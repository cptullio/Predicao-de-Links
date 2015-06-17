'''
Created on Jun 14, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets

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
        teste = []
        articlename = ''
        time = 0
        for line in self.OrignalContent:
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
                
                    
            if line.startswith('#!'):
                matches = (x for x in authorofArticles if x.articleid == articleid)
                for x in matches:
                    x.time = time      
                        
                        
        
        
            
            
        
        authorid = 0
        with open(self.filepathAuthorFormatted, 'w') as fautor:
            for x in authors:
                authorid = authorid + 1;
                fautor.write(str(authorid) + ';' + x + '\r\n')
            
        with open(self.filepathArticleFormatted, 'w') as fout:
            for article in articles:
                fout.write(str(article.articleid) + ';' + article.articlename + ';' + article.time + '\r\n')
            
        with open(self.filepathArticleAuthorFormatted, 'w') as fauthorarticleout:
            for author in authorofArticles:
                fauthorarticleout.write(str(author.articleid) + ';' + str(author.authorid)+ ';' + str(author.time) + '\r\n')
            
            
        
    def __init__(self, filepathOriginalDataSet, filepathArticleFormatted, filepathAuthorFormatted, filepathArticleAuthorFormatted):
        super(DBLPFormatingDataSets, self).__init__(filepathOriginalDataSet)
        self.filepathAuthorFormatted = filepathAuthorFormatted
        self.filepathArticleFormatted = filepathArticleFormatted
        self.filepathArticleAuthorFormatted = filepathArticleAuthorFormatted
        