#!/usr/bin/env python
import sys, json
from twython import Twython

tweetStr = sys.argv[1]

apiKey = 'API_KEY'
apiSecret = 'API_SECRET'
accessToken = 'ACCESS_TOKEN'
accessTokenSecret = 'ACCESS_TOKEN_SECRET'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweetStr)
