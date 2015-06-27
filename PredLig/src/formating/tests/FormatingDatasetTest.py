'''
Created on Jun 14, 2015

@author: cptullio
'''
import unittest
from os import path

class TestFormatting(unittest.TestCase):
    
	def get_abs_file_path(self,relativepath):
		script_path = path.abspath(__file__) 
		script_dir = path.split(script_path)[0]
		return path.join(script_dir, arquivo)
		
		
	
    
    def test_dblp_is(self):
		article = 'data/formatado/dblp_ai_article.txt'
		article = 'data/formatado/dblp_ai_article.txt'
		
		
		conteudo = None
		with open(abs_file_path) as f:
			conteudo = f.readlines()
			f.close()
		print conteudo
			
    
     
    

if __name__ == "__main__":
    unittest.main()