'''
Created on 24 de jun de 2015

@author: CarlosPM
'''
import unittest
from formating.dblp.Formating import Formating


class TestDBLP(unittest.TestCase):


    #Qty of Authors: 43578
    #Qty of Articles: 34340
    def test_ai_formating(self):
        teste = Formating(
                                      'data/original/DBLP_Citation_2014_May/domains/Artificial intelligence.txt',
                                      'data/formatado/dblp_ai_article.txt',
                                      'data/formatado/dblp_ai_author.txt',
                                      'data/formatado/dblp_ai_articlearthor.txt'
		                              )
        teste.readingOrginalDataset()
        
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()