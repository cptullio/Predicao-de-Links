'''
Created on 24 de jun de 2015

@author: CarlosPM
'''
import unittest
from formating.dblp.Formating import Formating


class TestDBLP(unittest.TestCase):


    def test_ai_formating(self):
        teste = Formating(
                                      'D:/mestrado_git/Predicao-de-Links/PredLig/src/data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt',
                                      'D:/mestrado_git/dblp_ai_article.txt',
                                      'D:/mestrado_git/dblp_ai_author.txt',
                                      'D:/mestrado_git/dblp_ai_articlearthor.txt'
                                      
                                      
                                      )
        teste.readingOrginalDataset()
        
    def test_full_formating(self):
        teste = Formating(
                                      'D:/mestrado_git/publications.txt',
                                      'D:/mestrado_git/dblp_full_article.txt',
                                      'D:/mestrado_git/dblp_full_author.txt',
                                      'D:/mestrado_git/dblp_full_articlearthor.txt'
                                      
                                      
                                      )
        teste.readingOrginalDataset()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()