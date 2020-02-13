#!/usr/bin/env python
import sys, json
from twython import Twython

# takes in the system argument as the tweet
# this will be used like this:
# python tweeter.py "This string will be tweeted"
tweetStr = sys.argv[1]

apiKey = 'API KEY HERE'
apiSecret = 'API SECRET HERE'
accessToken = 'ACCESS TOKEN HERE'
accessTokenSecret = 'ACCESS TOKEN SECRET HERE'

# sends tweet
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)