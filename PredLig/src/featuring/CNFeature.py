'''
Created on Jun 17, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase

class CNFeature(FeatureBase):
    '''
    Common Neighbors
    '''
    def __init__(self):
        super(CNFeature, self).__init__()

    def execute(self, node1, node2):
        neighbors_node1 = self.generate_all_node_neighborsfromNode1(node1)
        neighbors_node2 = self.generate_all_node_neighborsfromNode2(node2)
        
        return len(neighbors_node1.intersection(neighbors_node2))

    def __repr__(self):
        return 'cn'
            