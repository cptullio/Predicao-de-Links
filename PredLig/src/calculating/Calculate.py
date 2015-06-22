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
        type_nodes = set(n for n,d in self.preparedParameter.graph.nodes(data=True) if d['type'] == 'N')
        missing_nodes = self.preparedParameter.featuresChoice[0].get_pair_node_not_linked(type_nodes)
        print missing_nodes
        for missing_node in missing_nodes:
            result = Result(missing_node.first_node, missing_node.second_node,
                            self.preparedParameter.featuresChoice[0].all_node_neighbors(missing_node.first_node),
                            self.preparedParameter.featuresChoice[0].all_node_neighbors(missing_node.second_node), [])
            for item_feature in self.preparedParameter.featuresChoice:
                result.calcs.append(item_feature.execute(result.current_neighbor_node1,result.current_neighbor_node2))
            self.results.append(result)
        