'''
Created on Jun 14, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx

class Article(object):
    
    def __init__(self, articleid, name, time):
        self.articleid = articleid
        self.articlename = name
        self.time = time
        self.authors = set()

class Author(object):
    
    def __init__(self, authorid, name):
        self.authorid = authorid
        self.name = name
      

class DBLPFormatingDataSets(FormatingDataSets):



    
    def readingOrginalDataset(self):
        with open(self.OriginalDataSet) as f:
            self.OrignalContent = f.readlines()
        articleid = 0    
        articles = []
        article = None
        authors = set()
        for line in self.OrignalContent:
            line = line.strip()
            if line.startswith('#*'):
                articleid = articleid+1
                articlename = line.replace('#*','').replace('\r\n','').decode("latin-1")
            if line.startswith('#t'):
                time = line.replace('#t','').replace('\r\n','')
                article = Article(articleid, articlename, time)
                
            if line.startswith('#@'):
                authorsdesorder = line.replace('#@','').replace('\r\n','').split(',')
                for author in authorsdesorder:
                    authors.add(author)
                    
                    article.authors.add(autor)
            if line.startswith('#!'):
                articles.append(article)     

                
        self.graph = networkx.Graph()
        for article in articles:
            for author in article.authors:
                others = article.authors - set(author)
                for other in others:
                    self.graph.add_edge(autor, other, {'time': article.time})
        
        
        networkx.write_graphml(self.graph, self.filepathGraph)     
            
        
    def __init__(self, filepathOriginalDataSet, filepathGraph):
        super(DBLPFormatingDataSets, self).__init__(filepathOriginalDataSet)
        self.filepathGraph = filepathGraph
        