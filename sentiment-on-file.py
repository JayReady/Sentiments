from textblob import TextBlob
import sys



f = open('text/buzz/buzz_0006.txt', 'r')
print f

print "\n The text says:"

paragraph = f.read()
print paragraph

print "\n Analysis:\n"


print TextBlob(paragraph).sentiment
print "\n done \n" ## Sentiment(polarity=-0.3076923076923077, subjectivity=0.5769230769230769)



