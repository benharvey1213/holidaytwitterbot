import liker

file = open("./todaysTweets.txt")
tweets = file.read().split("\n")

for tweet in tweets:
	if tweet != "":
		liker.like(tweet)

