'''
Created on Jul 2, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx
from datetime import datetime


class Analyse(object):

    def __init__(self, preparedParameters, filePathResults, filePathAnalyseResult):
        print "Starting Analysing the results", datetime.today()
        
        absFilePath = filePathResults
        absfilePathAnalyseResult = filePathAnalyseResult #FormatingDataSets.get_abs_file_path(filePathAnalyseResult)
        fResult = open(absFilePath, 'r')
        with open(absfilePathAnalyseResult, 'w') as fnodes:
            success = 0
            element = 0
            for line in fResult:
                element = element+1
                FormatingDataSets.printProgressofEvents(element, preparedParameters.top_rank, "Analysing the results: ")
                cols = line.strip().replace('\n','').split('\t')
                if len(list(networkx.common_neighbors(preparedParameters.testGraph, cols[len(cols)-2] ,  cols[len(cols)-1] ))) != 0:
                    success = success + 1
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'SUCCESS \r\n')
                else:
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'FAILED \r\n')
                
                
                
                if element == preparedParameters.top_rank:
                    break 
            
            result =  float(success) / float(preparedParameters.top_rank) *100
            strResult = 'Final Result: \t' + str(result) + '%'
            fnodes.write(strResult)
            fnodes.close()
        print "Analysing the results finished", datetime.today()
      
            






