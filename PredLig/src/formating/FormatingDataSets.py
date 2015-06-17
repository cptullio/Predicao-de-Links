'''
Created on Jun 14, 2015

@author: cptullio
'''
from abc import abstractmethod

class FormatingDataSets(object):
    '''
    classdocs
    '''
    @abstractmethod      
    def readingOrginalDataset(self):
        raise RuntimeError('not implemented')
    
    
    def __init__(self, filePathOriginalDataSet):
        self.OriginalDataSet = filePathOriginalDataSet
        
        