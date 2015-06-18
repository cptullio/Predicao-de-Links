'''
Created on Jun 16, 2015

@author: cptullio
'''
import networkx
from calculating.Result import Result

class Calculate(object):
    '''
    Calculate
    '''


    def __init__(self, preparedParameter):
        self.preparedParameter = preparedParameter
        
        self.results = []
        for current_edge in self.preparedParameter.graph.edges():
            neighbors_node1 = self.preparedParameter.featuresChoice[0].all_neighbors(current_edge[0])
            neighbors_node2 = self.preparedParameter.featuresChoice[0].all_neighbors(current_edge[1])
            result = Result(current_edge[0], current_edge[1], neighbors_node1, neighbors_node2 , [])
            for item_feature in self.preparedParameter.featuresChoice:
                result.calcs.append(item_feature.execute(neighbors_node1,neighbors_node2))
            self.results.append(result)
        