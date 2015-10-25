
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

pages = {
    u'buzz': u'http://www.buzzfeed.com/',
    u'daim': u'http://www.dailymail.co.uk/ushome/index.html',
    u'nyti': u'http://www.nytimes.com/',
    u'wiki': u'https://en.wikipedia.org/wiki/Main_Page',
}

html_folder = u'html'
text_folder = u'text'

if not os.path.exists(html_folder):
    os.makedirs(html_folder)

for source, page in pages.items():

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