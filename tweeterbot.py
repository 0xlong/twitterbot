import tweepy
import time
import requests
from bs4 import BeautifulSoup

quote_page = 'https://api.binance.com/api/v1/ticker/price?'
hdr = {'User-Agent': 'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(quote_page,hdr).text, 'html.parser')

consumer_key = 'I7dpeQOATsugQ16dX3edQPR3e'
consumer_secret = '9PA24qlo0SMadnhw7gYGLymJD660KDUgfOqMQaFH54hyBxlrWo'
access_token = '937601962077573120-N1rBZ0fxIxee0vFL0G7JbCmWQcQGlox'
access_token_secret = 'rQcorRCJas682sDAcCjIkx9mANVadhHI4Sek32jPhVXmJ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

numer=len(requests.get(quote_page,hdr).text)

api.update_status(status=numer)
time.sleep(5)
api.update_status(status=(numer+1))
time.sleep(5)
api.update_status(status=(numer+2))
