"""
Written by JayReady using TextBlob
https://textblob.readthedocs.org/en/dev/
"""

from textblob import TextBlob
import sys

print "\nNEWS NOT NOISE!\n"
print '\nNumber of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

print "\n Analysis:\n"

sentence = str(sys.argv)

print TextBlob(sentence).sentiment
print "\n done \n" ## Sentiment(polarity=-0.3076923076923077, subjectivity=0.5769230769230769)

