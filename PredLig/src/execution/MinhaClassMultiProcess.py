
import urllib
import time
import feedparser

# Base api query url
base_url = 'http://export.arxiv.org/api/query?';

# Search parameters
search_query = 'cat:astro-ph*+AND+submittedDate:[200401010000+TO+200406312359]' # search for electron in all fields
start = 0                       # start at the first result
total_results = 4481           # want 20 total results
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
