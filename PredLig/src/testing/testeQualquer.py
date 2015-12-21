'''
Created on Dec 19, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse
import networkx
from formating import FormatingDataSets
from os import path
import os

            
if __name__ == '__main__':
    
    
    relativepath  = 'data/results/teste/file.txt'
    FormatingDataSets.FormatingDataSets.get_abs_file_path(relativepath)
   
    
    
