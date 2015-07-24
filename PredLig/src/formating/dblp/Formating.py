'''
Created on 24 de jun de 2015

@author: CarlosPM
'''
from formating.FormatingDataSets import FormatingDataSets
from formating.dblp.Article import Article
from formating.dblp.Author import Author
from formating.dblp.AuthorInArticle import AuthorInArticle
import networkx
from datetime import datetime

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
			line = line.strip()
			if line.startswith('#*'):
				articleid = articleid+1
				article = Article('p_' + str(articleid))
				article.articlename = line.replace('#*','').replace('\r\n','')
			if line.startswith('#t'):
				article.time = line.replace('#t','').replace('\r\n','')
			
			if line.startswith('#@'):
				authorsofArticle = line.replace('#@','').replace('\r\n','').split(',')
				for author in authorsofArticle:
					author = author.strip()
					if not author in authornames:
						authornames.append(author)
					articleauthor = AuthorInArticle(article.articleid, authornames.index(author)+1)
					authorofArticles.append(articleauthor)
			if line.startswith('#!'):
				articles.append(article)
		for index in range(len(authornames)):
			author = Author(index+1, authornames[index])
			authors.append(author)
		graph = networkx.Graph()
		for item_article in articles:
			graph.add_node(item_article.articleid, {'node_type' : 'E', 'title' : item_article.articlename.decode("latin_1"), 'time' : int(item_article.time) })
		for item_author in authors:
			graph.add_node(int(item_author.authorid), {'node_type' : 'N', 'name' : item_author.name.decode("latin_1") })
		for item_edge in authorofArticles:
			graph.add_edge(item_edge.articleid, int(item_edge.authorid) )
		
		return graph
	
	@staticmethod
	def get_graph_from_period(graph, t0,t0_):
		
		print "Getting Papers", datetime.today()
		papers = list([n,d] for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and d['time'] >= t0 and d['time'] <= t0_)
		print "Total Papers: ",  len(papers),  datetime.today()
		new_graph = networkx.Graph()
		new_graph.add_nodes_from(papers)
		for paper in papers:
			authors = networkx.all_neighbors(graph, paper[0])
			for author in authors:
				author_withData = list([n,d] for n,d in graph.nodes(data=True) if n == author)
				new_graph.add_nodes_from(author_withData)
				new_graph.add_edge(paper[0], author)
		return new_graph
	
					

	def __init__(self, filepathOriginalDataSet, graphfile):
	
		super(Formating, self).__init__(filepathOriginalDataSet)
	
		graph = self.readingOrginalDataset()

		networkx.write_graphml(graph, self.get_abs_file_path(graphfile)) 
			
			
			
		