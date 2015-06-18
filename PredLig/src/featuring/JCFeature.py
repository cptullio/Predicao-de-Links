'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase

class JCFeature(FeatureBase):
    '''
    Jaccard Coefficient
    '''


    def __init__(self):
        super(JCFeature, self).__init__()

    def execute(self, neighbor_node1, neighbor_node2):
        return len(neighbor_node1.intersection(neighbor_node2))/len(neighbor_node1.union(neighbor_node2))
