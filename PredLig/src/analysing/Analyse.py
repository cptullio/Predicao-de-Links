'''
Created on Jul 2, 2015

@author: cptullio
'''
from formating.FormatingDataSets import FormatingDataSets
import networkx

class Analyse(object):
    '''
    classdocs
    '''


    def __init__(self, preparedParameters, filePathResults):
        absFilePath = FormatingDataSets.get_abs_file_path(filePathResults)
        lines = FormatingDataSets.reading_file(absFilePath)
        for i in range(preparedParameters.top_rank):
            clean_line = lines[i].strip().replace('\r\n','')
            cols = clean_line.split('\t')
            
            if preparedParameters.testGraph.has_edge(cols[len(preparedParameters.featuresChoice)],cols[len(preparedParameters.featuresChoice)+1] ):
                print cols[len(preparedParameters.featuresChoice)], cols[len(preparedParameters.featuresChoice)+1], 'ok'
            else:
                print cols[len(preparedParameters.featuresChoice)], cols[len(preparedParameters.featuresChoice)+1], 'fail'
            
        
        