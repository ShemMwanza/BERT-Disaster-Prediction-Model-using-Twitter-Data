# DistilBERT-Disaster-Prediction-Model-using-Twitter-Data

Disaster occurrences in Kenya have been a norm over the years, from landslides and floods to
violence and spreading of diseases. These disasters have caused a dent in the economy and
uncertainties in the country and its people. Through Twitter, disaster information can be
captured in real-time, and this information can be vital to first responders in making rescue
plans and creating situational awareness for better disaster management. Therefore, Twitter can
be used to create a way for prediction of disasters.

This project aims to provide a way of predicting disasters through use of Twitter data. The goal
is to develop a model that will be able to predict disasters occurring using Twitter data. This
model will be based on distilled Bidirectional Encoder Representation from Transformers (DistilBERT).
BERT has a bidirectional nature that allows it to understand meaning of words based on context
in any direction of the sequence of the words.

The methodology that will be used in this project will be the Agile development methodology
with scrum approach as it will allow the project to be divided into several sprints that will be
manageable and understandable. The project will follow the OOAD design paradigm that will
allow viewing of the whole project from the point of objects as they function and interact.

# Description of the Dataset
The dataset used in this project is obtained from Kaggle, from the Natural Language Processing with Disaster Tweets competition that contains 10876 tweets. The dataset is split into a train set and a test set.
The train set contains approximately 7613 annotated tweets as well as additional features such as id, keyword, and location. The annotations are of two classes, (1) for Disaster-related and (0) for Not disaster-related.
The test set contains approximately 3263 tweets having only the id as the other feature. The test set is suitable for performing predictions as it does not contain the target. 
The train set was split further in an 80:20 ratio to form a new train set and validation set, respectively. The validation set had approximately 1523 tweets with the new train set having 6090 tweets.

# Data Cleaning
The quality of each sentence in the dataset was too noisy to fine tune the model. Therefore, elements in the texts such as emojis, meta data, and URLs could have affected the performance of the model negatively. Data cleaning was necessary to create a suitable form of text prior to fine tuning. The steps taken to clean the data were:
i.	Removing URLs
ii.	Removing emojis
iii.	Removing punctuations
iv.	Removing HTML data
v.	Making tweets to be lowercase

# Tokenization
Tokenization involves converting text input to tokens. After data cleaning, the next step in preprocessing is tokenization of the input texts. The tokenizer used was the DistilBert Tokenizer that works with DistilBert for tokenization tasks using the tokenizer.encode_plus() function. This function returned the actual input ids, the attention masks, and the token type ids in a dictionary but the token type ids are set to false because DistilBert does not require them.
The first task was to insert the [CLS] token at the start and the [SEP] token at the end of each input text. The sentences are padded with [PAD] tokens until the total length equals the truncated maximum length. The maximum length of each sentence was set at 50 hence, padding is added in case sentences are shorter to make up the length.
# Description of Training and Validation

# Description of Model
The model used in this project is DistilBERT Base uncased. It is a pretrained distilled version of the BERT model, but it is smaller, faster and requires less memory than BERT. The model is uncased thus does not make a difference between sentences in different cases. 
A neural network was created for fine tuning. The neural network had the DistilBERT model followed by a dropout layer, a linear layer and activation layer to obtain output. Input was fed into the model based on the dataset. The model was finally instantiated and finally used for training of the model.

# Creating Dataloaders
After creating the neural network and instantiating the model object, the next step was to use a dataloader to create training and validation dataloaders. The dataloaders were required to load data into the neural network in a specific order. This was necessary because the data could not be loaded into memory all at once. As a result, the amount of data loaded into memory and then passed to the neural network had to be defined. The parameters batch size and max length were used to control the amount of data. The batch size and maximum length values were 32 and 50, respectively.

# Training
In the next step, the loss function was defined, its purpose was to calculate the difference in the output created by the model and the actual output. An optimizer was also defined, and its purpose was to update the weights of the neural network to improve its performance. The optimizer used was Adaptive Moment Estimation with Weight Decay (AdamW).

# Fine tuning
A training function was defined when it came to fine tuning. Its purpose was to train the model on the train set. It had 6 parameters, namely: the model, the train set, the validation set, the learning rate, number of epochs and the batch size.
The batch size was essential to creating the dataloaders, the number of epochs defined the number of times the data was going to be passed through the network. The learning rate was a hyper parameter that defined the adjustments of weights of the network with respect to the loss gradient descent. The learning rate used in fine-tuning 1e-6.
Subsequent output from the model and the actual label are compared to calculate the loss. The loss value is used to optimize the weights of the neurons in the network.
After every epoch, the train loss value is recorded. In addition to this, the train accuracy is also recorded and displayed in a line graph. The train accuracy achieved after 16 epochs was 0.868 while the train loss was 0.336.
# Validation
Validation dataset is used to evaluate the performance of the model. The model has not seen this data during training. The data was loaded onto the neural network using the dataloader with 32 as the batch size. During the validation stage the weights of the model were not updated. Only the final output was compared to the actual value.
After every epoch, the validation loss value is recorded. In addition to this, the validation accuracy is also recorded and displayed in a line graph. The validation accuracy achieved after 16 epochs was 0.839 while the validation loss was 0.392.
Once the validation was completed in every epoch the model was saved, this enabled the model to be loaded from the very last saving point instead of retraining and revalidating.


# System Implementation

i.  Index Page

![image](https://user-images.githubusercontent.com/77288876/209867304-5e0e3062-9bfc-4189-8a2b-dff4d050de3f.png)


ii.	Request Twitter Data using Keyword Page 
The user is able to input a keyword to fetch tweets containing the keyword as displayed

![image](https://user-images.githubusercontent.com/77288876/209866731-9ee6b56f-bb81-46ac-8a6a-07c081d6c2c5.png)

iii.	Prediction on multiple Twitter Data Page
The user receives fetched tweets with prediction based on the keyword that was entered as displayed.

![image](https://user-images.githubusercontent.com/77288876/209866757-444c114b-1fe3-44a0-a4d9-7a6c6a206706.png)

iv.	Predict Single Tweet String Page
The user is able to input a tweet and receive a prediction based on the string as displayed.

![image](https://user-images.githubusercontent.com/77288876/209866791-adea71da-c221-416f-8bef-324d1955140f.png)



