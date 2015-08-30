'''
Created on Jul 2, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx
from datetime import datetime


class Analyse(object):

    @staticmethod
    def getTopRank(relativeFilePathRandomAnalised):
        absFile = FormatingDataSets.get_abs_file_path(relativeFilePathRandomAnalised)
        f = open(absFile, 'r')
        for last in f:
            pass
        return int(last.split('\t')[1])
        
    @staticmethod
    def getTopRankABSPathFiles(absoluteFilePathAnalysed):
        f = open(absoluteFilePathAnalysed, 'r')
        for last in f:
            pass
        return int(last.split('\t')[1])
    
    @staticmethod
    def getLastInfosofResultsABSPathFiles(absoluteFilePathAnalysed, TopRank):
        f = open(absoluteFilePathAnalysed, 'r')
        line = 0
        info = []
        for last in f:
            line = line +1
            if line > TopRank:
                info.append(last)
            pass
        return info[0].split('\t')[1]
    
        
    
    def __init__(self, preparedParameters, filePathResults, filePathAnalyseResult, topRank):
        print "Starting Analysing the results", datetime.today()
        
        absFilePath = filePathResults
        absfilePathAnalyseResult = filePathAnalyseResult #FormatingDataSets.get_abs_file_path(filePathAnalyseResult)
        fResult = open(absFilePath, 'r')
        with open(absfilePathAnalyseResult, 'w') as fnodes:
            self.success = 0
            element = 0
            for line in fResult:
                element = element+1
                FormatingDataSets.printProgressofEvents(element, topRank, "Analysing the results: ")
                cols = line.strip().replace('\n','').split('\t')
                if len(list(networkx.common_neighbors(preparedParameters.testGraph, cols[len(cols)-2] ,  cols[len(cols)-1] ))) != 0:
                    self.success = self.success + 1
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'SUCCESS \r\n')
                else:
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'FAILED \r\n')
                
                
                
                if element == topRank:
                    break 
            
            result =  float(self.success) / float(topRank) *100
            strResult = 'Final Result: \t' + str(result) + '%'
            fnodes.write(strResult)
            fnodes.write('\n#\t'+str(self.success))
            fnodes.close()
        print "Analysing the results finished", datetime.today()
      
            






