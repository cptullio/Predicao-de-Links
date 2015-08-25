'''
Created on Aug 23, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import urllib
import xml.dom.minidom
import time
import feedparser
import networkx
import gc

    
class Formating(FormatingDataSets):
    '''
    classdocs
    '''
    
    def __init__(self, graphfile):
    
        super(Formating, self).__init__('',graphfile)
        
    def get_qty_records_mid_year(self,year):
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

    def get_articles(self,search_query, start, total_results,results_per_iteration):
        base_url = 'http://export.arxiv.org/api/query?'
        new_article = []
        inicio = start
        for i in range(inicio,total_results,results_per_iteration):
            print "Results %i - %i" % (i,i+results_per_iteration)
    
            query = 'search_query=%s&start=%i&max_results=%i' % (search_query,i,results_per_iteration)
            
            response = urllib.urlopen(base_url+query).read()
            print 'Parsing response'
            feed = feedparser.parse(response)
            
            papers = feed.entries
            print (base_url+query), 'results: ', len(papers)
        
            for entry in papers:
                idpaper = str('%s' % entry.id.split('/abs/')[-1])
                title = str(entry.title.encode("utf-8"))
                yearPublication = int(entry.published.split('-')[0])
                authors = set()
                categories = ()
                print entry.category
                print entry.category
                
                for c in entry.categories:
                    print c
                for a  in entry.authors:
                    authors.add(a.name.encode("utf-8"))
                
                data = [idpaper, title,  yearPublication,  authors ] 
                new_article.append(data)
               
      
            # Remember to play nice and sleep a bit before you call
            # the api again!
            print 'Sleeping for 10 seconds' 
            time.sleep(10)
        return new_article

    
    
    def readingOrginalDataset(self):
        #yearstoRescue = [2005,]
        yearstoRescue = [2012,2013,2014]
        
        for year in  yearstoRescue:
            articles = []
            qty = self.get_qty_records_mid_year(year);
            print qty
            search_queryMid = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'01010000+TO+'+str(year)+'06312359]' # search for electron in all fields
            search_queryfinal = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'07010000+TO+'+str(year)+'12312359]' # search for electron in all fields
            print "getting Begin"
            begin = None
            element = 0
            while True:
                element = element+1
                begin = self.get_articles(search_queryMid, 0, qty[0], 2)
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
                final = self.get_articles(search_queryfinal, 0, qty[1], 2000)
                if len(final) == qty[1]:
                    break
                else:
                    print 'Did not get everything... trying again...', element, len(final)
                if element == 3:
                    print 'Did not work exit everything'
                    exit()
            for j in final:
                articles.append(j)
            
            f = open(self.get_abs_file_path(self.GraphFile) + '.' +str(year) + '.txt', 'w')
            for item in articles:
                f.write(item[0] + '\t' + item[1] + '\t' + str(item[2]) + '\t' + repr(item[3] ) + '\n')
            f.close()
            articles = None
            del articles
            
                
                
        
                
            
    