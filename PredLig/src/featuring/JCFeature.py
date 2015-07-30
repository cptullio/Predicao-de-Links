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

    def execute(self, node1, node2):
        neighbors_node1 = self.generate_all_node_neighborsfromNode1(node1)
        neighbors_node2 = self.generate_all_node_neighborsfromNode2(node2)
        #print node1, node2, neighbors_node1, neighbors_node2
        f = (float)(len(neighbors_node1.intersection(neighbors_node2)))
        x = (float)(len(neighbors_node1.union(neighbors_node2)))
        if x == 0:
            return 0
        return f/x
