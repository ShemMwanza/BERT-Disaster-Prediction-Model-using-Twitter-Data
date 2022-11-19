from flask import Flask, render_template, request, redirect, url_for
from receiveTweets import fetch_Tweets
from bert import predict
import string
import re
import torch 
import torch.optim as optim
import torch.nn.functional as F
from torch import nn
from torchvision import transforms
import numpy as np
import pandas as pd
from torch.optim import lr_scheduler
from csv import reader
from werkzeug.utils import secure_filename
import os
import sched, time
s = sched.scheduler(time.time, time.sleep)

app = Flask(__name__)
IMG_FOLDER = os.path.join('assets')

app.config['FOLDER'] = IMG_FOLDER

class BertClassifier(nn.Module):

  def __init__(self, bert):
    super(BertClassifier, self).__init__()
    self.bert = bert
    self.drop = nn.Dropout(0.5)
    self.relu = nn.ReLU()
    self.out = nn.Linear(self.bert.config.hidden_size, 2)

  def forward(self, input_ids, mask):
    _, pooled_output = self.bert(input_ids, attention_mask=mask, return_dict=False)
    output = self.drop(pooled_output)
    output= self.out(output)
    return self.relu(output)

model = torch.load('./Model/model.bin')
#Declaring of hyperparameters
batch_size = 32

"""# **Data Cleaning**"""

def remove_URLs(text):  #removing URLs
	url = re.compile(r'https?://\S+|www\.\S+')
	return url.sub(r'', text)

def remove_emojis(text):  #removing emojis
	emoji_pattern = re.compile(
		'['
		u'\U0001F600-\U0001F64F' 
		u'\U0001F300-\U0001F5FF'  
		u'\U0001F680-\U0001F6FF'  
		u'\U0001F1E0-\U0001F1FF'  
		u'\U00002702-\U000027B0'
		u'\U000024C2-\U0001F251'
		u'\U0001f926-\U0001f937'
		u'\U00010000-\U0010ffff'
		']+', # emoticons, symbols etc
		flags=re.UNICODE)
	return emoji_pattern.sub(r'', text)

def remove_punctuations(text): #removing punctuations
	table = str.maketrans('', '', string.punctuation)
	return text.translate(table)

def remove_html_data(text):   #removing HTML data
	html = re.compile(r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	return re.sub(html, '', text)

def fetchData(query):
	tweets = fetch_Tweets(query)

	tweets['tweet_text'] = tweets['tweet_text'].apply(lambda x: remove_URLs(x))
	tweets['tweet_text'] = tweets['tweet_text'].apply(lambda x: remove_emojis(x))
	tweets['tweet_text'] = tweets['tweet_text'].apply(lambda x: remove_html_data(x))
	tweets['tweet_text'] = tweets['tweet_text'].apply(lambda x: remove_punctuations(x))
	tweets['prediction'] = predict(model,tweets['tweet_text'].values,batch_size)
	return tweets

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route('/predict')
def predictPage():
    return render_template('predict.html')

@app.route('/predict', methods=['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        user = request.form['search']
        return redirect(url_for('success', query=user))

@app.route('/search/<query>')
def success(query):
	html = pd.DataFrame.from_dict(fetchData(query)).to_html()
	results = "<div id='kk'>" + html + " </div> "
	# time.sleep(10)
	return render_template('result.html', results = results)

@app.route('/stringpredict')
def stringPredictPage():
    return render_template('stringPredict.html')
@app.route('/stringpredict', methods=['POST', 'GET'])
def stringpredict():
	if request.method == 'POST':
		string = request.form['strings']
		df = pd.DataFrame([string], columns=['text'])
		df['text'] = df['text'].apply(lambda x: remove_URLs(x))
		df['text'] = df['text'].apply(lambda x: remove_emojis(x))
		df['text'] = df['text'].apply(lambda x: remove_html_data(x))
		df['text'] = df['text'].apply(lambda x: remove_punctuations(x))
		df['predict'] = predict(model,df['text'].values,1)
		if (df['predict'].values == 1 ):
			result = 'This is a Disaster tweet'
		else:
			result = 'This is not a Disaster Tweet'
		
		return render_template('stringPredict.html', result= result)

if __name__ == '__main__':
	app.run(debug=True)
