'''
Created on Jul 2, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx


class Analyse(object):

    def __init__(self, preparedParameters, filePathResults, filePathAnalyseResult):
        absFilePath = FormatingDataSets.get_abs_file_path(filePathResults)
        absfilePathAnalyseResult = FormatingDataSets.get_abs_file_path(filePathAnalyseResult)
        lines = FormatingDataSets.reading_file(absFilePath)
        with open(absfilePathAnalyseResult, 'w') as fnodes:
            success = 0
            for i in range(preparedParameters.top_rank):
                clean_line = lines[i].strip().replace('\r\n','')
                cols = clean_line.split('\t')
                if networkx.common_neighbors(preparedParameters.testGraph, cols[len(cols)-2],cols[len(cols)-1] ) != 0:
                    success = success + 1
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'SUCCESS \r\n')
                else:
                    fnodes.write(cols[len(cols)-2]  + '\t' + cols[len(cols)-1] + '\t' +  'FAILED \r\n')
            
            result =  float(success) / float(preparedParameters.top_rank) *100
            strResult = 'Final Result: \t' + str(result) + '%'
            fnodes.write(strResult)
            fnodes.close()






