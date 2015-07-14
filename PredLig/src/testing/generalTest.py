import unittest

from formating.dblp.Formating import Formating
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from parametering.ParameterUtil import ParameterUtil
import networkx
import matplotlib
import numpy
from datetime import datetime
from featuring.FeatureBase import FeatureBase




#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
	
	def get_YearsofArticles(self, graph, node1, node2):
		result = []
		for node in networkx.common_neighbors(graph, node1, node2):
			for n,d in graph.nodes(data=True):
				if n == node:
					result.append(d['time'])
		result.sort(reverse=True)
		return result
	
	
	def test_viewingexemplomenor(self):
		util = ParameterUtil(parameter_file = 'data/parameter.txt')
		graph = networkx.read_graphml(Formating.get_abs_file_path(util.graph_file))
		networkx.draw_networkx(graph)
		matplotlib.pyplot.show()
		
	
	def test_creating_TimeScoreOriginal(self):
		util = ParameterUtil(parameter_file = 'data/parameter_timescore.txt')
		graph = networkx.read_graphml(Formating.get_abs_file_path(util.trainnig_graph_file))
		pair_nodes_not_linked = VariableSelection(graph, util.nodes_notlinked_file)
		justOneFeature = FeatureBase()
		justOneFeature.graph = graph
		for pair in pair_nodes_not_linked.results:
			pair_common_neighbors  = justOneFeature.get_common_neighbors(pair[0], pair[1])
			articles = []
			for pair_common_neighbor in pair_common_neighbors:
				articles.append(self.get_YearsofArticles(graph, pair[0], pair_common_neighbor))
				articles.append(self.get_YearsofArticles(graph, pair[1], pair_common_neighbor))
			print articles
			#Harmonic Mean of Publications
			total = float(0)
			for years in articles:
				total = total + 1/float(len(years))
			hm = len(pair) / total
			print hm
			#Decay Function
			k =  int(datetime.today().year)  - int(max(list(articles))[0])
			decayfunction = (1 - util.decay) ** k
			print decayfunction
			timescore = (hm * decayfunction) / (abs( max(list(articles[0])) - max(list(articles[1])))  + 1)
			print timescore
			
			
		#networkx.draw_networkx(graph)
		#matplotlib.pyplot.show()
	
		
	
	def test_getnolinknodes(self):
		results = []
		util = ParameterUtil(parameter_file = 'data/parameter_timescore.txt')
		myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
		authors =set(n for n,d in myparams.trainnigGraph.nodes(data=True) if d['node_type'] == 'N')
		for author in authors:
			others =  authors - set(author)
			for other_author in others:
				if len(set(networkx.common_neighbors(myparams.trainnigGraph, author, other_author))) == 0:
					isAlreadyThere = 0
					for n in results:
						if n[0] == author and n[1] == other_author:
							isAlreadyThere = isAlreadyThere + 1
						if n[1] == author and n[0] == other_author:
							isAlreadyThere = isAlreadyThere + 1
					if isAlreadyThere == 0:
						results.append([author, other_author ]) 
					
		print results
	
	
	def test_generateTimeScore(self):
		results = []
		util = ParameterUtil(parameter_file = 'data/parameter_timescore.txt')
		myDblpFormating = Formating(util.original_file, util.graph_file)
		myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
		authors =list([n,d] for n,d in myparams.trainnigGraph.nodes(data=True) if d['node_type'] == 'N')
		for author in authors:
			papers_of_author = set(networkx.all_neighbors(myparams.trainnigGraph, author[0]))
			for paper in papers_of_author:
				coAuthors = set(networkx.all_neighbors(myparams.trainnigGraph,paper)) - set(author[0])
				for coAuthor in coAuthors:
					print author[0], coAuthor
					isAlreadyThere = 0
					for n in results:
						if n[0] == author[0] and n[1] == coAuthor:
							isAlreadyThere = isAlreadyThere + 1
						if n[1] == author[0] and n[0] == coAuthor:
							isAlreadyThere = isAlreadyThere + 1
					if isAlreadyThere == 0:
						results.append([author[0], coAuthor ])
		print results    
			
	def test_viewgraph(self):
		
		util = ParameterUtil(parameter_file = 'data/parameter_timescore.txt')
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.trainnig_graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.trainnig_graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.test_graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.test_graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		
		
if __name__ == "__main__":
	unittest.main()