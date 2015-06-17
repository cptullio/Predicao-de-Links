'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase

class PAFeature(FeatureBase):
    '''
    Preference Attachment
    '''

    def __init__(self):
        super(PAFeature, self).__init__()

    def execute(self, neighbor_node1, neighbor_node2):
        return len(neighbor_node1) * len(neighbor_node2)
    