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

    def execute(self, neighbor_node1, neighbor_node2):
        return len(neighbor_node1.intersection(neighbor_node2))

            