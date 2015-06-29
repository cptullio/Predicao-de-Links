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
    
    def test_reading_ai_graph(self):
        graph_file = 'data/formatado/dblp_ai_graph.txt'
        graph = networkx.read_graphml(Formating.get_abs_file_path(graph_file))
        all_papers = list(d['time'] for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
        qtde = 0;
        sum = 0;
        print set(sorted(all_papers))
        for year in all_papers:
            qtde = qtde+1;
            sum = sum + int(year);
        print sum;
        print qtde;
        print sum / qtde;
         
    
    def test_generating_graph(self):

        original = 'data/original/DBLP_Citation_2014_May/domains/ExemploMenor.txt'
        article = 'data/formatado/dblp_exemploMenor_article.txt'
        author = 'data/formatado/dblp_exemploMenor_author.txt'
        edge_file = 'data/formatado/dblp_exemploMenor_articlearthor.txt'
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        
        myformat = Formating(original, article, author, edge_file, graph_file)
        networkx.draw_networkx(myformat.fullGraph)
        plt.show()
        
    def test_reading_graph(self):
        graph_file = 'data/formatado/dblp_exemploMenor_graph.txt'
        graph = Formating.reading_graph(graph_file)
        print graph.nodes(data=True)
        
        all_papers = list(d['time'] for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
        
        print all_papers
        
        qtde = 0;
        sum = 0;
        for year in all_papers:
            qtde = qtde+1;
            sum = sum + int(year);
        print sum;
        print qtde;
        print sum / qtde;
        
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()