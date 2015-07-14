'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import numpy as numpy


class AASFeature(FeatureBase):
    '''
    adamic adar similarity
    '''
    def __repr__(self):
        return 'aas'
    
    def __init__(self):
        super(AASFeature, self).__init__()

    def execute(self, node1, node2):
    
        neighbors_node1 = self.generate_all_node_neighborsfromNode1(node1)
        neighbors_node2 = self.generate_all_node_neighborsfromNode2(node2)
        measure = 0
        for neighbor in neighbors_node1.intersection(neighbors_node2):
            secondary_neighbors = self.all_neighbors(neighbor)
            measure += 1 / (numpy.log10(len(secondary_neighbors)))
        return measure
            