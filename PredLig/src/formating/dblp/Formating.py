'''
Created on 24 de jun de 2015

@author: CarlosPM
'''
from formating.FormatingDataSets import FormatingDataSets
from formating.dblp.Article import Article
from formating.dblp.Author import Author
from formating.dblp.AuthorInArticle import AuthorInArticle


class Formating(FormatingDataSets):
  
    def readingOrginalDataset(self):
        with open(self.OriginalDataSet) as f:
            self.OrignalContent = f.readlines()
            f.close()
        
        articleid = 0
        articles = []
        authornames = []
        authorofArticles = []
        authors = []
        article = None
        for line in self.OrignalContent:
            #clearing the line
            line = line.strip()
            #begin of article
            if line.startswith('#*'):
                articleid = articleid+1
                article = Article(articleid)
                article.articlename = line.replace('#*','').replace('\r\n','')
            #rescue the year of the article
            if line.startswith('#t'):
            
                article.time = line.replace('#t','').replace('\r\n','')
            
            if line.startswith('#@'):
                #rescue all authors of that article
                authorsofArticle = line.replace('#@','').replace('\r\n','').split(',')
                for author in authorsofArticle:
                    #check if that author is already in array of authors  
                    if not author in authornames:
                        authornames.append(author)
                    articleauthor = AuthorInArticle(articleid, authornames.index(author)+1)
                    authorofArticles.append(articleauthor)
            
            #end of article
            if line.startswith('#!'):
                articles.append(article)
                
        for index in range(len(authornames)):
            author = Author(index+1, authornames[index])
            authors.append(author)
            
        print "Qty of Authors: " + str(len(authors))
        print "Qty of Articles: " + str(len(articles))
        
        with open(self.filepathAuthorFormatted, 'w') as fautor:
            for x in authors:
                if x.name == '':
                    x.name = 'Nothing Recorded'
                fautor.write(str(x.authorid) + '\t' + x.name + '\r\n')
            
        with open(self.filepathArticleFormatted, 'w') as farticle:
            for article in articles:
                farticle.write(str(article.articleid) + '\t' + article.articlename + '\t' + article.time + '\r\n')
            
        with open(self.filepathArticleAuthorFormatted, 'w') as fauthorarticleout:
            for author in authorofArticles:
                fauthorarticleout.write(str(author.articleid) + '\t' + str(author.authorid) + '\r\n')
        
        

    def __init__(self, filepathOriginalDataSet, filepathArticleFormatted, filepathAuthorFormatted, filepathArticleAuthorFormatted):
        super(Formating, self).__init__(filepathOriginalDataSet)
        self.filepathAuthorFormatted = self.get_abs_file_path(filepathAuthorFormatted)
        self.filepathArticleFormatted = self.get_abs_file_path(filepathArticleFormatted)
        self.filepathArticleAuthorFormatted = self.get_abs_file_path(filepathArticleAuthorFormatted)
        