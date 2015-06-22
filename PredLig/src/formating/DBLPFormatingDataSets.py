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

class AuthorArticle(object):
    
    def __init__(self, articleid, authorid):
        self.authorid = authorid
        self.articleid = articleid
        self.time = 0

class DBLPFormatingDataSets(FormatingDataSets):



    
    def readingOrginalDataset(self):
        with open(self.OriginalDataSet) as f:
            self.OrignalContent = f.readlines()
        articleid = 0
        articles = []
        authors = []
        authorofArticles = []
        articlename = ''
        for line in self.OrignalContent:
            line = line.strip()
            if line.startswith('#*'):
                articleid = articleid+1
                articlename = line.replace('#*','').replace('\r\n','')
            if line.startswith('#t'):
                time = line.replace('#t','').replace('\r\n','')
                article = Article(articleid, articlename, time)
                articles.append(article)
                
            if line.startswith('#@'):
                authorsdesorder = line.replace('#@','').replace('\r\n','').split(',')
                for autor in authorsdesorder:
                    if not autor in authors:
                        authors.append(autor)
                    articleauthor = AuthorArticle(articleid, authors.index(autor)+1)
                    authorofArticles.append(articleauthor)
                  
        authorid = 0
        self.graph = networkx.Graph()
        for author in authors:
            authorid = authorid+1
            self.graph.add_node(authorid, {'name' : author.decode("latin-1"), 'type' : 'N' })
        
        for article in articles:
            self.graph.add_node(article.articleid, {'name' : article.articlename.decode("latin-1"), 'time' : article.time, 'type': 'E' })
        
        for item in authorofArticles:
            self.graph.add_edge(item.articleid, item.authorid)
        
        networkx.write_graphml(self.graph, self.filepathGraph)     
            
        
    def __init__(self, filepathOriginalDataSet, filepathGraph):
        super(DBLPFormatingDataSets, self).__init__(filepathOriginalDataSet)
        self.filepathGraph = filepathGraph
        