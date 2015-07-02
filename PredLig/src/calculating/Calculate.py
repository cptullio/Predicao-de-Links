'''
Created on Jun 16, 2015

@author: cptullio
'''
import networkx
from formating.dblp.Formating import Formating

class Calculate(object):
    '''
    Calculate
    '''


    def __init__(self, preparedParameter, selecting, filepathResult):
        self.preparedParameter = preparedParameter
        featuresOrderedbyScalar = sorted(self.preparedParameter.featuresChoice, key=lambda color: color[1], reverse=True)
        calculateResults = []
        for item in selecting.results:
            neighbors_node1 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[0]))
            neighbors_node2 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[1]))
            item_result = []
            
            for calc in featuresOrderedbyScalar:
                item_result.append(  { str(calc) : calc[0].execute(neighbors_node1,neighbors_node2) * calc[1]})
            calculateResults.append([n for n in item_result, item[0], item[1]])
        myfile = Formating.get_abs_file_path(filepathResult)
        self.orderedCalculateResult = sorted(calculateResults, reverse=True)
        with open(myfile, 'w') as fnodes:
            for item in self.orderedCalculateResult:
                for calc in item[0]:
                    fnodes.write(str(calc) + '\t')
                fnodes.write(str(item[1]) +  '\t' +str(item[2]) +'\r\n')
            
        
            
          
            