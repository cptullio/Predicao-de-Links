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
    ScoreResult =[]
    result = [ [1,2,[8,2,3,4] ], [2,3,[5,6,7,8]]  ]
    count = len(result)
    for index in range(4):  
        scoreOrder = sorted(result, key=lambda value: value[2][index], reverse=False)
        
        ScoreResult.append(scoreOrder)
    print ScoreResult
   
    
    
