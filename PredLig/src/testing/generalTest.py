import unittest

import networkx
from formating.dblp.Formating import Formating
import matplotlib
from networkx.classes.function import neighbors

#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
    
    def test_reading_graph(self):
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        print "Reading full graph"
        graph = Formating.reading_graph(graph_file)
        print "generate simple graph"
        new_graph = Formating.get_graph_without_paper_nodes(graph)
        print "saving simple graph"
        networkx.write_graphml(new_graph, Formating.get_abs_file_path('data/formatado/dblp_exemploMenor_new_graph.txt'))
    
    def test_separating_graph(self):
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        simple_graph_file = 'data/formatado/dblp_exemploMenor_new_graph.txt'
        
        graph = Formating.reading_graph(graph_file)
        simple_graph = Formating.reading_graph(simple_graph_file)
        
        time_media = Formating.get_media_year_papers(graph)
        print time_media
        training = list([n,d,f] for n,d,f in simple_graph.edges(data=True) if f['time'] <=time_media+1)
        test = list([n,d,f] for n,d,f in simple_graph.edges(data=True) if f['time'] >time_media+1)
        
        print training
        print test
        trainingGraph = networkx.Graph()
        for curr_edge in training:
            trainingGraph.add_edge(curr_edge[0], curr_edge[1], curr_edge[2])
        results = []
        all_authorsTrainnig = set(trainingGraph.nodes())
        
        for curr_node in all_authorsTrainnig:
            others =  all_authorsTrainnig - set(networkx.all_neighbors(trainingGraph, curr_node))
            others.remove(curr_node)
            for other_node in others:
                isAlreadyThere = 0
                for n in results:
                    if n[1] == curr_node and n[2] == other_node:
                        isAlreadyThere = isAlreadyThere + 1
                    if n[2] == curr_node and n[1] == other_node:
                        isAlreadyThere = isAlreadyThere + 1
                
                if isAlreadyThere == 0:
                    neighbor_node1 = set(networkx.all_neighbors(trainingGraph, curr_node))
                    neighbor_node2 = set(networkx.all_neighbors(trainingGraph, other_node))
            
                    results.append([len(neighbor_node1.intersection(neighbor_node2)), curr_node,other_node ]) 
        
        
        #for item in results:
        #    print item
         
        results.sort(cmp=None, key=None, reverse=True)
        print results
        
                
                       
                       
        
        #networkx.draw_networkx(trainingGraph)
        #matplotlib.pyplot.show()
            
            
            
        
        
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()