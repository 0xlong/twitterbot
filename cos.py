import tweepy

consumer_key = 'msLJGoIZx7hMxWv6eszGGOBfi'
consumer_secret = 'azXQeRpFj9Wowfnrhj1M4CcMgVm5Kp9SXhppPNx26MfLHHivUA'
access_token = '3914186835-ml58nTscOP4TbwuDK1U2aA0YiA1PtlOjlUMPrJH'
access_token_secret = 'JqJdbB4Hj9U52iiEQ1yxDpn2xPxMs0wlx8i3ncCna75LE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweet = "yop"
api.update_status(status=tweet)

# Below are some examples of what we can now do -- just uncomment the relevant lines to run



# Uncomment the next line to send the above tweet:




# Uncomment the next 3 lines to print the last 20ish tweets from @_hacksu:OR SOME CRYPTOBOTS

# tweets = api.user_timeline('_hacksu')
# for i in tweets:
#     print (i.text)