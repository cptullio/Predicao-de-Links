import unittest

import networkx
from formating.dblp.Formating import Formating
import matplotlib.pyplot as plt

#python -m unittest GeneralTestings

class GeneralTest(unittest.TestCase):
    
    def test_generating_ai_graph(self):

        original = 'data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt'
        article = 'data/formatado/dblp_ai_article.txt'
        author = 'data/formatado/dblp_ai_author.txt'
        edge_file = 'data/formatado/dblp_ai_articlearthor.txt'
        graph_file = 'data/formatado/dblp_ai_graph.txt'
        
        myformat = Formating(original, article, author, edge_file, graph_file)
    
    def test_generating_graph(self):

        original = 'data/original/DBLP_Citation_2014_May/domains/ExemploMenor.txt'
        article = 'data/formatado/dblp_exemploMenor_article.txt'
        author = 'data/formatado/dblp_exemploMenor_author.txt'
        edge_file = 'data/formatado/dblp_exemploMenor_articlearthor.txt'
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        
        myformat = Formating(original, article, author, edge_file, graph_file)
        networkx.draw_networkx(myformat.fullGraph)
        plt.show()
        
    def test_reading_ai_graph(self):
        graph_file = 'data/formatado/dblp_ai_graph.txt'
        graph = Formating.reading_graph(graph_file)
        new_graph = Formating.get_graph_without_paper_nodes(graph)
        print 'Gerando Grafo'
        networkx.write_graphml(new_graph, Formating.get_abs_file_path('data/formatado/dblp_ai_newgraph.txt'))
        
    
    def test_reading_graph(self):
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        graph = Formating.reading_graph(graph_file)
        networkx.draw_networkx(Formating.get_graph_without_paper_nodes(graph))
        plt.show()
        
        
        
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()