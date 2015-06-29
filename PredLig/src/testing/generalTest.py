import unittest

import networkx
from formating.dblp.Formating import Formating

#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
	
	def test_reading_ai_graph(self):
		graph_file = 'data/formatado/dblp_ai_graph.txt'
   		print "Reading full graph"
		graph = Formating.reading_graph(graph_file)
		print "generate simple graph"
		new_graph = Formating.get_graph_without_paper_nodes(graph)
		print "saving simple graph"
		networkx.write_graphml(new_graph, Formating.get_abs_file_path('data/formatado/dblp_ai_newgraph.txt'))
        
        
        
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()