'''
Created on Jul 2, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx
from datetime import datetime
import formating


class Analyse(object):



    @staticmethod
    def AnalyseNodesInFuture(nodesToChecked, TestGraph):
        result = []
        for nodeToCheck in nodesToChecked:
            if (TestGraph.has_edge(nodeToCheck[0],nodeToCheck[1])):
                result.append([  nodeToCheck[0],nodeToCheck[1], 1 ])
            else:
                result.append([  nodeToCheck[0],nodeToCheck[1], 0 ])
        return result
    
    
    @staticmethod
    def saving_analyseResult(AnalysedNodesnotLinkedInFuture, filepath):
        f = open(FormatingDataSets.get_abs_file_path(filepath), 'w')
        f.write('no1,no2,result\n')
        
        for item in AnalysedNodesnotLinkedInFuture:
            value = ''
            for item_index in range(len(item)):
                value = value  + repr(  item[item_index]  )
                if (item_index < len(item)):
                    value = value + ','
            final = value + '\n'
            
            f.write( final.replace(',\n', '\n')  )
        f.close()   

    @staticmethod
    def reading_analyseResult( filepath):
        result = []
        firstLine = 0
        f = open(FormatingDataSets.get_abs_file_path(filepath), 'r')
        for line in f:
            if firstLine == 0:
                firstLine = 1
                continue
            cols = line.strip().replace('\n','').split(',')
            item_result = []
            for col in cols:
                try:
                    item_result.append(eval(col))
                except Exception:
                    item_result.append(str(col))
            result.append(item_result)
        return result
            
    
    @staticmethod
    def get_topRank(AnalyseNodesnotLinkedInFuture):
        return len(  list([n1,n2] for n1,n2,result in AnalyseNodesnotLinkedInFuture if result ==1 ) )
        
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
    
        
    
