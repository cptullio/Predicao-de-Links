import unittest
from os import path
import networkx

#python -m unittest GeneralTestings

class GeneralTestings(unittest.TestCase):
    
	def get_abs_file_path(self,relativepath):
		script_path = path.abspath(__file__) 
		script_dir = path.split(script_path)[0]
		return path.join(script_dir, relativepath)
	
	def reading_file(self, abs_file):
		content = None
		with open(abs_file) as f:
			content = f.readlines()
			f.close()
		return content
		

	def test_generating_graph(self):
		f_article = self.get_abs_file_path('data/formatado/dblp_ai_article.txt')
		f_author = self.get_abs_file_path('data/formatado/dblp_ai_author.txt')
		f_edge = self.get_abs_file_path('data/formatado/dblp_ai_articleauthor.txt')
		
		f_article_content = self.reading_file(f_article)
		f_author_content = self.reading_file(f_author)
		f_edge_content = self.reading_file(f_edge)
		graph = networkx.Graph()
		
		for article_line in f_article_content:
			article_line = article_line.strip()
			cols = article_line.split(";")
			graph.add_node(cols[0], {'node_type': 'E', 'title' : cols[1], 'time' : int(cols[2]) })
		
		for author_line in f_author_content:
			author_line = author_line.strip()
			cols = author_line.split(";")
			graph.add_node(cols[0], {'node_type': 'N', 'name' : cols[1] })
		
		for edge_line in f_edge_content:
			edge_line = edge_line.strip()
			cols = edge_line.split(";")
			graph.add_edge(cols[0], cols[1] )
		
		all_Authors = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
		all_Papers = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'E')
		all_Papers_2000 = set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and d['time'] > 2000)
		print len(all_Papers_2000)
		
		
			
		
		
		
		
		
		
		
		
    
     
    

if __name__ == "__main__":
    unittest.main()