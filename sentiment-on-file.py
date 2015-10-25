from textblob import TextBlob
import sys

print "\ngetting started\n"

for num in range(0,9):

	try:

		filepath = 'text/buzz/buzz_000%i.txt' %num
		f = open(filepath, 'r')
#		print f

		paragraph = f.read()

#		for line in paragraph:
#			try:

				#print "\n The text says:"
				#print line
				#print "\n Analysis:\n"

		TextBlob(str(paragraph)).sentiment
				#print "\n done \n" ## Sentiment(polarity=-0.3076923076923077, subjectivity=0.5769230769230769)

		f.close()

	except:
		print "%s didn't work" %str(filepath)

	else: 
		print "Sentiment in %s: %s" %(str(filepath), TextBlob(paragraph).sentiment)
