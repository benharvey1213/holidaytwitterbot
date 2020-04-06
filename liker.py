import sys, json
from twython import Twython

apiKey = 'API_KEY'
apiSecret = 'API_SECRET'
accessToken = 'ACCESS_TOKEN'
accessTokenSecret = 'ACCESS_TOKEN_SECRET'

twitter = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

def like(tweetStr):
	search = twitter.search(q=tweetStr, result_type="recent", count=100)

	favs = []

	favsResponse = twitter.get_favorites(count=50)

	for fav in favsResponse:
	    favs.append(fav['id'])

	count = 0

	for status in search['statuses']:
	    id = status['id']
	    try:
	        if id not in favs:
	            twitter.create_favorite(id=id)
	            count = count + 1
	    except:
	        break

	print('Liked ' + str(count) + ' tweets from ' + tweetStr)
