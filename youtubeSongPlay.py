# from __future__ import division
from datetime import datetime
import requests
from lxml import html, etree
import json
from textblob import TextBlob
import pandas as pd 
import matplotlib.pyplot as plt 
import warnings
import webbrowser as wb
import speech_recognition as sr 

r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)

    try:
        spoken = r.recognize_google(audio)
        print('You said: {}'.format(spoken))
    except:
        print('Sorry, could not understand your voice')

# warnings.filterwarnings('ignore')
pd.options.display.max_columns = 100
pd.options.display.max_rows = 20
pd.options.display.width = 120

# Get key from Google Developer's Console
api_key = 'AIzaSyBVuuRbSK8dAlGg6Cct0tdSDtl6Ff6j1fk'
url = 'https://www.googleapis.com/youtube/v3/search'

parameters = {'part': 'snippet',
                'maxResults': 1,
                'q': spoken,
                'key': api_key,
                'type': 'video',
            }

page = requests.request(method='get', url=url, params=parameters)
j_results = json.loads(page.text)
# print(page.text)

vidID = j_results['items'][0]['id']['videoId']
# print(vidID)

vidBaseUrl = 'https://www.youtube.com/watch?v='

wb.open(vidBaseUrl+vidID)


