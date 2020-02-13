# This program should be run every morning
# It will schedule cron jobs that will be tweeted

# imports
from crontab import CronTab
from pushbullet import Pushbullet
import csv, datetime, time

# Pushbullet API key to send notifications to my phone
pb = Pushbullet('PUSHBULLET API KEY HERE')

# cron object to manage crontab jobs
cron = CronTab(user='pi')

# arrays to store the contents of the tweets and the times they are to be sent
tweets = []
tweetTimes = []

# grabs the current date to pull only the holidays from today
now = datetime.datetime.now()
#now = datetime.date(2020, 1, 1)

# first, delete all the old tweeter.py cron jobs
print('removing jobs...')
for job in cron:
	if "tweeter.py" in job.command:
		cron.remove(job)
		print(job.command)

# parse the notholidays csv and populate the tweets array with today's tweets
print('\nadding jobs...')
with open('/home/pi/notholidays.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if int(row[0]) == now.month and int(row[1]) == now.day:
			tweetContent = row[2]
			tweetHashtag = '#' + row[2].replace(' ','')
			tweetHashtag = tweetHashtag.replace("'", '')
			finalTweet = "" +  tweetContent + " is not a real holiday. " + tweetHashtag
			tweets.append(finalTweet)
			print(finalTweet)
		line_count += 1

# for notifactions
tweetString = ''
tweetsLength = len(tweets)

# schedule times
if tweetsLength == 1:
	tweetTimes.append(datetime.time(12, 0, 0))
elif tweetsLength == 2:
	tweetTimes.append(datetime.time(10, 0, 0))
	tweetTimes.append(datetime.time(14, 0, 0))
elif tweetsLength == 3:
	tweetTimes.append(datetime.time(10, 0, 0))
	tweetTimes.append(datetime.time(12, 0, 0))
	tweetTimes.append(datetime.time(14, 0, 0))
elif tweetsLength == 4:
	tweetTimes.append(datetime.time(9, 0, 0))
	tweetTimes.append(datetime.time(11, 0, 0))
	tweetTimes.append(datetime.time(13, 0, 0))
	tweetTimes.append(datetime.time(15, 0, 0))
elif tweetsLength == 5:
	tweetTimes.append(datetime.time(9, 0, 0))
	tweetTimes.append(datetime.time(10, 30, 0))
	tweetTimes.append(datetime.time(12, 0, 0))
	tweetTimes.append(datetime.time(13, 30, 0))
	tweetTimes.append(datetime.time(15, 0, 0))
elif tweetsLength == 6:
	tweetTimes.append(datetime.time(9, 0, 0))
	tweetTimes.append(datetime.time(10, 0, 0))
	tweetTimes.append(datetime.time(11, 0, 0))
	tweetTimes.append(datetime.time(12, 0, 0))
	tweetTimes.append(datetime.time(13, 0, 0))
	tweetTimes.append(datetime.time(14, 0, 0))
elif tweetsLength == 7:
	tweetTimes.append(datetime.time(9, 0, 0))
	tweetTimes.append(datetime.time(10, 0, 0))
	tweetTimes.append(datetime.time(11, 0, 0))
	tweetTimes.append(datetime.time(12, 0, 0))
	tweetTimes.append(datetime.time(13, 0, 0))
	tweetTimes.append(datetime.time(14, 0, 0))
	tweetTimes.append(datetime.time(15, 0, 0))
else:
	pb.push_note('ERROR: More than 7 tweets today')

# for task scheduling
for tweet in range(len(tweets)):
	# tweetString is only used for Pushbullet notifications
	tweetString += (tweets[tweet] + '\n')

	# thisTweet is the actual contents of the tweet
	thisTweet = tweets[tweet]

	# generates a new cron job with the tweet
	job = cron.new(command='python /home/pi/tweeter.py "' + thisTweet + '"')

	# sets the cron job time
	job.hour.on(tweetTimes[tweet].hour)
	job.minute.on(tweetTimes[tweet].minute)

	# adds the job to the cron file
	cron.write()

# notification handling
if (len(tweets) == 0):
	pb.push_note('No tweets today (' + str(now.month) + '/' + str(now.day) + ')' , '')
elif (len(tweets) == 1):
	pb.push_note('Today\'s Tweet (' + str(now.month) + '/' + str(now.day) + '):', tweetString)
else:
	pb.push_note('Today\'s Tweets (' + str(now.month) + '/' + str(now.day) + '):', tweetString)
