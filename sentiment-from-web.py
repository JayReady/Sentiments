from textblob import TextBlob
import sys
import os
try:
    # Python 2 compat
    from urllib2 import Request, build_opener
except ImportError:
    # Python 3
    from urllib.request import Request, build_opener

import lxml.html
from lxml.etree import ElementTree
import numpy as np


"""
Scrape the website and create textfiles in a html_folder
"""

page = str(sys.argv[1])
source = "temp"

html_folder = 'html'
text_folder = 'text'


if not os.path.exists(html_folder):
    os.makedirs(html_folder)

try:
#for counter in range(0,10):

    text_source_folder = os.path.join(text_folder, source)
    if not os.path.exists(text_source_folder):
        os.makedirs(text_source_folder)

    opener = build_opener()
    html_filename = os.path.join(html_folder, source + '.html')
    if not os.path.exists(html_filename):
        print("Downloading %s" % page)
        request = Request(page)
        # change the User Agent to avoid being blocked by Wikipedia
        # downloading a couple of articles ones should not be abusive
        request.add_header('User-Agent', 'OpenAnything/1.0')
        html_content = opener.open(request).read()
        open(html_filename, 'wb').write(html_content)

    # decode the payload explicitly as UTF-8 since lxml is confused for some
    # reason
    html_content = open(html_filename).read()
    if hasattr(html_content, 'decode'):
        html_content = html_content.decode('utf-8')
    tree = ElementTree(lxml.html.document_fromstring(html_content))
    i = 0
    j = 0
    for p in tree.findall('//p'):
        content = p.text_content()
        if len(content) < 100:
            # skip paragraphs that are too short - probably too noisy and not
            # representative 
            continue

        text_filename = os.path.join(text_source_folder,
                                     '%s_%04d.txt' % (source, i))
        print("Writing %s" % text_filename)
        open(text_filename, 'wb').write(content.encode('utf-8', 'ignore'))
        i += 1

except:
 	print ":("
 	pass
else:
 	print "\nSuccessfully downloaded something!\n"


"""
Read and analyze the text files one by one
"""


print "\n Let's get started with the analysis\n"

overall_score = []

for num in range(0,12):

	try:

		filepath = 'text/%s/%s_000%i.txt' %(source,source,num)
		f = open(filepath, 'r')
#		print f

		paragraph = f.read()


#		for line in paragraph:
#			try:

				#print "\n The text says:"
				#print line
				#print "\n Analysis:\n"

		TextBlob(paragraph).sentiment
				#print "\n done \n" ## Sentiment(polarity=-0.3076923076923077, subjectivity=0.5769230769230769)

		f.close()

	except:
		print "%s didn't work" %str(filepath)

	else:
            print "Subjectivity in %s: %s" %(str(filepath), TextBlob(paragraph).sentiment[1]) 
            newsenti = str(TextBlob(paragraph).sentiment[1])
            overall_score.append(newsenti)
            print overall_score
        
       # print type(TextBlob(paragraph).sentiment)
      #  overall_score.append(TextBlob(paragraph).sentiment)



#	except:
#		print "nope"

#	else: 
#		print "yay!"

