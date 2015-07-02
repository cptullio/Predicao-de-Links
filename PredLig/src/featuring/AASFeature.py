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

    def execute(self, neighbor_node1, neighbor_node2):
        measure = 0
        for neighbor in neighbor_node1.intersection(neighbor_node2):
            secondary_neighbors = self.all_neighbors(neighbor)
            measure += 1 / (numpy.log10(len(secondary_neighbors)))
        return measure
            