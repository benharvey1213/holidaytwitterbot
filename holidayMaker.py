import random, os

a = os.popen('wc -l ./data/singular-nouns.txt')
b = os.popen('wc -l ./data/plural-nouns.txt')
c = os.popen('wc -l ./data/adjectives.txt')

singNounCount = int(a.read().split(' ')[0])
plurNounCount = int(b.read().split(' ')[0])
adjCount = int(c.read().split(' ')[0])

aLine = random.randint(0, singNounCount)
bLine = random.randint(0, plurNounCount)
cLine = random.randint(0, adjCount)

aWord = os.popen('sed \'' + str(aLine) + "!d\' ./data/singular-nouns.txt").read().strip()
bWord = os.popen('sed \'' + str(bLine) + "!d\' ./data/plural-nouns.txt").read().strip()
cWord = os.popen('sed \'' + str(cLine) + "!d\' ./data/adjectives.txt").read().strip()

cWord = cWord.capitalize()


formattedAWord = ''

for word in range(0, len(aWord.split(' '))):
	formattedAWord += aWord.split(' ')[word].capitalize()

hashtag = '#National' + str(cWord) + formattedAWord + 'Day'

tweet = 'It might as well be ' + hashtag + ' today.'

os.popen('python tweeter.py \'' + tweet + '\'')
