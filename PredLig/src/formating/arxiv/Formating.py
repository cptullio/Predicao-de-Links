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
        yearstoRescue = [2005]
        #yearstoRescue = [2005,2006,2007,2008,2009, 2010,2011]
        articles = []
        authornames= []
        for year in  yearstoRescue:

            qty = self.get_qty_records_mid_year(year);
            print qty
            search_queryMid = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'01010000+TO+'+str(year)+'06312359]' # search for electron in all fields
            search_queryfinal = 'cat:astro-ph*+AND+submittedDate:['+str(year)+'07010000+TO+'+str(year)+'12312359]' # search for electron in all fields
            print "getting Begin"
            begin = None
            element = 0
            while True:
                element = element+1
                begin = self.get_articles(search_queryMid, 0, qty[0], 1000)
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
                final = self.get_articles(search_queryfinal, 0, qty[1], 1000)
                if len(final) == qty[1]:
                    break
                else:
                    print 'Did not get everything... trying again...', element, len(final)
                if element == 3:
                    print 'Did not work exit everything'
                    exit()
            for j in final:
                articles.append(j)
        
        self.Graph = networkx.Graph()
        for item_article in articles:
            self.Graph.add_node(item_article[0], {'node_type' : 'E', 'title' : item_article[1], 'time' : item_article[2] })
            for item_author in item_article[3]:
                if not item_author in authornames:
                    authornames.append(item_author)
                authorid = authornames.index(item_author)+1
                self.Graph.add_node(int(authorid), {'node_type' : 'N', 'name' : item_author })
                self.Graph.add_edge(item_article[0], int(authorid) )
                
                
        
                
            
    