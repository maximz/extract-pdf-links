# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 01:49:21 2012
Task: Given the URL of an HTML page, extract all links to PDF files contained within the page. Then write these links in a format that can be fed into your favorite download manager.

@author: Maxim Zaslavsky
"""

import sys, os, re, urllib

# Initialize: handle required arguemnts
try:
    urlsource, destinationfile = sys.argv[1], sys.argv[2]
except:
    print 'Incorrect arguments supplied. First argument must be URL of input page. Second argument must be destination for file to which output will be apended. Optional third argument: delimiter (default is new line).'
    sys.exit(1)
    
# Handle optional third argument
try:
    delim = sys.argv[3]
except:
    delim = '\n'

# Step 1: download HTML
html = urllib.urlopen(urlsource).read()
print 'Downloaded HTML'

# Step 2: extract links
m = re.findall(r'(?i)(https?://)(.+?)(\.pdf)', html) # match pdf links, e.g. http://any-text-here.com/something.pdf
print 'Located PDF links'

# Step 3: write links
formatstr = "%s"+delim
with open(destinationfile, 'a') as f: # append to file
    for item in m:
        output = ''.join(item) # combine all parts of the link
        f.write(formatstr % output) # or print>>thefile, item. note from documentation of os module that \n should be used on all platforms: http://docs.python.org/2/library/os.html#os.linesep
        
print 'Wrote to file'
print 'Done.'