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
		edges_found = list([n,d,f] for n,d,f in graph.edges(data=True) if f['time'] >= t0 and f['time'] <= t0_ )
		new_graph = networkx.Graph()
		for curr_edge in edges_found:
			new_graph.add_edge(curr_edge[0], curr_edge[1], curr_edge[2])
		return new_graph
	
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
					

	def __init__(self, filepathOriginalDataSet, graphfile):
	
		super(Formating, self).__init__(filepathOriginalDataSet)
	
		graph = self.readingOrginalDataset()
	
		s_graph = Formating.get_graph_without_paper_nodes(graph)
	
		networkx.write_graphml(s_graph, self.get_abs_file_path(graphfile)) 
			
			
			
		