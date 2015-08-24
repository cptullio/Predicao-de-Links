'''
Created on Aug 23, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import urllib
    
class Formating(FormatingDataSets):
    '''
    classdocs
    '''
    
    def __init__(self, graphfile):
    
        super(Formating, self).__init__('',graphfile)
    
    def readingOrginalDataset(self):
        url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
        data = urllib.urlopen(url).read()
        print data
