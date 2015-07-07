'''
Created on 24 de jun de 2015

@author: CarlosPM
'''
from formating.FormatingDataSets import FormatingDataSets
from formating.dblp.Article import Article
from formating.dblp.Author import Author
from formating.dblp.AuthorInArticle import AuthorInArticle
import networkx


class Formating(FormatingDataSets):
	
	def generating_graph(self):
		f_article_content = self.reading_file(self.filepathArticleFormatted)
		f_author_content = self.reading_file(self.filepathAuthorFormatted)
		f_edge_content = self.reading_file(self.filepathArticleAuthorFormatted)
		graph = networkx.Graph()

        for article_line in f_article_content:
            article_line = article_line.strip()
            cols = article_line.split("\t")
            graph.add_node(cols[0], {'node_type' : 'E', 'title' : cols[1].decode("latin_1"), 'time' : int(cols[2]) })
        
        for author_line in f_author_content:
            author_line = author_line.strip()
            cols = author_line.split("\t")
            graph.add_node(int(cols[0]), {'node_type' : 'N', 'name' : cols[1].decode("latin_1") })
      
        for edge_line in f_edge_content:
            edge_line = edge_line.strip()
            cols = edge_line.split("\t")
            graph.add_edge(cols[0], int(cols[1]) )
        return graph

  
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
                    author = author.strip() 
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
                farticle.write('p_' + str(article.articleid) + '\t' + article.articlename + '\t' + article.time + '\r\n')
            
        with open(self.filepathArticleAuthorFormatted, 'w') as fauthorarticleout:
            for author in authorofArticles:
                fauthorarticleout.write('p_' + str(author.articleid) + '\t' + str(author.authorid) + '\r\n')

				
				
    @staticmethod      
    def get_media_year_papers(graph):
        all_papers = list(d['time'] for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
        sum_of_year_papers = 0;
        for year in all_papers:
            sum_of_year_papers = sum_of_year_papers + int(year);
        return sum_of_year_papers / len(all_papers);
    
    @staticmethod      
    def get_graph_without_paper_nodes(graph):
        all_authors = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        graph_clean = networkx.Graph()
        for author in all_authors:
            for intermediate_node in list(networkx.all_neighbors(graph, author)):
                time = int(list(d['time'] for n,d in graph.nodes(data=True) if n == intermediate_node)[0])
                for second_author in list( n for n in  networkx.all_neighbors(graph, intermediate_node) if n != author):
                    graph_clean.add_edge(author, second_author, {'time' : time})
        
        return graph_clean
    
    @staticmethod      
    def get_graph_from_period(graph, t0,t0_):
        edges_found = list([n,d,f] for n,d,f in graph.edges(data=True) if f['time'] >= t0 and f['time'] <= t0_ )
        new_graph = networkx.Graph()
        for curr_edge in edges_found:
            new_graph.add_edge(curr_edge[0], curr_edge[1], curr_edge[2])
        return new_graph
            
        

    def __init__(self, filepathOriginalDataSet,  graphfile = ''):
        super(Formating, self).__init__(filepathOriginalDataSet)
        self.readingOrginalDataset()
        self.graph = self.generating_graph()
        self.simple_graph = self.get_graph_without_paper_nodes(self.graph)
        if graphfile != '':
            networkx.write_graphml(self.simple_graph, self.get_abs_file_path(graphfile))