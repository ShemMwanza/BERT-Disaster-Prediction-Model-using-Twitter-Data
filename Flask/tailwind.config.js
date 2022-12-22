/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./js/styles/**/*.js",
    "./js/components/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        gray: {
          light: '#f9fbfb',
          DEFAULT: '#4A6163',
          lt: '#92acae',
          dark: '#4B6163',
        },
        black: {
          DEFAULT: '#000000',
        },
        white: {
          light: '#ffffff',
          DEFAULT: '#ffffff',
          dark: '#F2F2F2',
        },
        orange: {
          light: '#FEC9C9',
          DEFAULT: '#FD6585',
          dark: '#360940',
        },
        blue: {
          light: '#00EAFF',
          DEFAULT: '#3C8CE7',
          dark: '#0036FF',
        },
        green: {
          light: '#D1FAE5',
          DEFAULT: '#34D399',
          dark: '#ffffff',
        },
        yellow: {
          DEFAULT: '#FFC94B',
        },
        purple: {
          DEFAULT: '#0D25B9',
        }
      }
},
  },
  plugins: [],
}