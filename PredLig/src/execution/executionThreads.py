"""
python_arXiv_paging_example.py

This sample script illustrates paging of arXiv api 
results.  In order to play nice with the api, we 
recommend that you wait 3 seconds between api calls.

Please see the documentation at 
http://export.arxiv.org/api_help/docs/user-manual.html
for more information, or email the arXiv api 
mailing list at arxiv-api@googlegroups.com.

urllib is included in the standard python library.
feedparser can be downloaded from http://feedparser.org/ .

Author: Julius B. Lucks

This is free software.  Feel free to do what you want
with it, but please play nice with the arXiv API!
"""

import urllib
import time
import feedparser

# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
search_query = 'cat:astro-ph*+AND+submittedDate:[200401010000+TO+200412312359]' # search for electron in all fields
start = 0                       # start at the first result
total_results = 9254              # want 20 total results
results_per_iteration = 3000       # 5 results at a time
wait_time = 3                   # number of seconds to wait beetween calls

print 'Searching arXiv for %s' % search_query

astrophArtigcles = []

for i in range(start,total_results,results_per_iteration):
    
    print "Results %i - %i" % (i,i+results_per_iteration)
    
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                         i,
                                                        results_per_iteration)

    # perform a GET request using the base_url and query
    response = urllib.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)

    # Run through each entry, and print out information
    for entry in feed.entries:
        astrophArtigcles.append(str('%s' % entry.id.split('/abs/')[-1]))
        
      
    # Remember to play nice and sleep a bit before you call
    # the api again!
    print 'Sleeping for %i seconds' % wait_time 
    time.sleep(wait_time)
print len(astrophArtigcles)
