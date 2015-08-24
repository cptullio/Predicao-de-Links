'''

Created on Aug 2, 2015



@author: cptullio

'''

import urllib





import xml.dom.minidom
import time
import feedparser


 
def get_qty_records_mid_year(year):
    url = 'http://export.arxiv.org/api/query?search_query=cat:astro-ph*+AND+submittedDate:[' +str(year) + '01010000+TO+' +str(year)+ '06312359]&start=0&max_results=1'
    data = urllib.urlopen(url).read()
    xmldoc = xml.dom.minidom.parseString(data)
    qtyRecordsMid = int(xmldoc.getElementsByTagName('opensearch:totalResults')[0].childNodes[0].data)
    time.sleep(3)
    url = 'http://export.arxiv.org/api/query?search_query=cat:astro-ph*+AND+submittedDate:[' +str(year) + '07010000+TO+' +str(year)+ '12312359]&start=0&max_results=1'
    data = urllib.urlopen(url).read()
    xmldoc = xml.dom.minidom.parseString(data)
    qtyRecordsMidFinal = int(xmldoc.getElementsByTagName('opensearch:totalResults')[0].childNodes[0].data)
    time.sleep(3)
    return [qtyRecordsMid,qtyRecordsMidFinal]
         
def get_articles(search_query, start, total_results,results_per_iteration):
    base_url = 'http://export.arxiv.org/api/query?'
    new_article = []
    inicio = start
    for i in range(inicio,total_results,results_per_iteration):
        print "Results %i - %i" % (i,i+results_per_iteration)
    
        query = 'search_query=%s&start=%i&max_results=%i' % (search_query,i,
                                                        results_per_iteration)

        response = urllib.urlopen(base_url+query).read()

        feed = feedparser.parse(response)
        
        papers = feed.entries
        print (base_url+query), 'results: ', len(papers)
        
        for entry in papers:
            new_article.append(str('%s' % entry.id.split('/abs/')[-1]))
        
      
    # Remember to play nice and sleep a bit before you call
    # the api again!
        print 'Sleeping for 10 seconds' 
        time.sleep(10)
    return new_article

if __name__ == '__main__':

    yearstoRescue = [2004, 2005]
    articles = []
    for year in  yearstoRescue:

        qty = get_qty_records_mid_year(year);
        print qty
        #search_queryMid= 'cat:astro-ph*+AND+submittedDate:[200401010000+TO+200406312359]'
        #search_queryfinal= 'cat:astro-ph*+AND+submittedDate:[200407010000+TO+200412312359]'
        search_queryMid = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'01010000+TO+'+str(year)+'06312359]' # search for electron in all fields
        search_queryfinal = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'07010000+TO+'+str(year)+'12312359]' # search for electron in all fields
        print "getting Begin"
        begin = None
        element = 0
        while True:
            element = element+1
            begin = get_articles(search_queryMid, 0, qty[0], 2000)
            if len(begin) == qty[0]:
                break
            else:
                print 'Did not get everything... trying again...', element, len(begin)
            if element == 3:
                print 'Did not work exit everything'
                exit()
            
        for i in begin:
            articles.append(i)
        print "getting Final"
        final = None
        element = 0
        while True:
            final = get_articles(search_queryfinal, 0, qty[1], 2000)
            if len(final) == qty[1]:
                break
            else:
                print 'Did not get everything... trying again...', element, len(final)
            if element == 3:
                print 'Did not work exit everything'
                exit()
        for j in final:
            articles.append(j)
    
    print len(articles)    
