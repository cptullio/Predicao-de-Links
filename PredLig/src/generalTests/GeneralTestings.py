import unittest

import networkx
from formating.dblp.Formating import Formating

#python -m unittest GeneralTestings

class GeneralTestings(unittest.TestCase):
    
    def test_generating_graph(self):
        dblp_formating = Formating(
                                    'data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt',
                                    'data/formatado/dblp_ai_article.txt',
                                    'data/formatado/dblp_ai_author.txt',
                                    'data/formatado/dblp_ai_articlearthor.txt'
                                    )
        f_article_content = dblp_formating.reading_file(dblp_formating.filepathArticleFormatted)
        f_author_content = dblp_formating.reading_file(dblp_formating.filepathAuthorFormatted)
        f_edge_content = dblp_formating.reading_file(dblp_formating.filepathArticleAuthorFormatted)
        graph = networkx.Graph()
        
        
        
        for article_line in f_article_content:
            article_line = article_line.strip()
            cols = article_line.split("\t")
            graph.add_node(cols[0], {'node_type' : 'E', 'title' : cols[1].decode("latin_1"), 'time' : int(cols[2]) })
        
        for author_line in f_author_content:
            author_line = author_line.strip()
            cols = author_line.split("\t")
            graph.add_node(cols[0], {'node_type' : 'N', 'name' : cols[1] })
      
        for edge_line in f_edge_content:
            edge_line = edge_line.strip()
            cols = edge_line.split("\t")
            graph.add_edge(cols[0], cols[1] )
            
            
            
        all_Authors = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        all_Papers = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
        #all_Papers_2000 = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and d['time'] > 2000)
        print len(all_Authors)
        print len(all_Papers)
        #print len(all_Papers_2000)
        
        
if __name__ == "__main__":
    unittest.main()