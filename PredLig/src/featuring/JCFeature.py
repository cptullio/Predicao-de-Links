'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase

class JCFeature(FeatureBase):
    '''
    Jaccard Coefficient
    '''
    def __repr__(self):
        return 'jc'
    

    def __init__(self):
        super(JCFeature, self).__init__()

    def execute(self, neighbor_node1, neighbor_node2):
        f = (float)(len(neighbor_node1.intersection(neighbor_node2)))
        x = (float)(len(neighbor_node1.union(neighbor_node2)))
        return f/x
