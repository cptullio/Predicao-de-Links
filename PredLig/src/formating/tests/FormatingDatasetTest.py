'''
Created on Jun 14, 2015

@author: cptullio
'''
import unittest
from formating.DBLPFormatingDataSets import DBLPFormatingDataSets

class TestFormatting(unittest.TestCase):
    
    def test_dblp_ai(self):
        teste = DBLPFormatingDataSets(
                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt',
                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_article.txt',
                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_author.txt',
                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor.txt'
                                      
                                      
                                      )
        teste.readingOrginalDataset()
   
#def test_dblp_full(self):
#        teste = DBLPFormatingDataSets(
#                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/original/DBLP_Citation_2014_May/publications.txt',
#                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_full_article.txt',
#                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_full_author.txt',
#                                      '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_full_articlearthor.txt'
#                                      
#                                      
#                                      )
#        teste.readingOrginalDataset()


if __name__ == "__main__":
    unittest.main()