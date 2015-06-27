'''
Created on Jun 14, 2015

@author: cptullio
'''
from abc import abstractmethod
from os import path

class FormatingDataSets(object):
    
    def get_abs_file_path(self,relativepath):
        script_path = path.abspath(__file__) 
        print script_path
        script_dir = path.split(script_path)[0]
        return path.join(script_dir, relativepath)
    
    def reading_file(self, abs_file):
        content = None
        with open(abs_file) as f:
            content = f.readlines()
            f.close()
        return content


    @abstractmethod      
    def readingOrginalDataset(self):
        raise RuntimeError('not implemented')
    
    
    def __init__(self, filePathOriginalDataSet):
        self.OriginalDataSet = self.get_abs_file_path(filePathOriginalDataSet)
        
        