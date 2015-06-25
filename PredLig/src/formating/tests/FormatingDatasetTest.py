'''
Created on Jun 14, 2015

@author: cptullio
'''
import unittest
from formating.DBLPFormatingDataSets import DBLPFormatingDataSets
import networkx



class TestFormatting(unittest.TestCase):
    
    
    def test_dblp_is(self):
        
        
        teste = DBLPFormatingDataSets(
                                      'D:/mestrado_git/Predicao-de-Links/PredLig/src/data/original/DBLP_Citation_2014_May/domains/Information security.txt',
                                      'D:/is_graph.txt'
                                      
                                      )
        teste.readingOrginalDataset()
    
    def test_dblp_ai(self):
        
        
        teste = DBLPFormatingDataSets(
                                      '/Users/cptullio/predLig-carlospedro/Predicao-de-Links/PredLig/src/data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt',
                                      '/Users/cptullio/ai_graph.txt'
                                      
                                      )
        teste.readingOrginalDataset()
    
     
    

if __name__ == "__main__":
    unittest.main()