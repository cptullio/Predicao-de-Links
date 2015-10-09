'''
Created on Oct 4, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase

class WCNFeature(FeatureBase):
    '''
    Weighted Common Neighbor by Linyuan Lu and Tao
    '''
    def __repr__(self):
        return 'WCN'
    

    def __init__(self):
        super(WCNFeature, self).__init__()
        self.debugar = False
        
    
    
    
    def execute(self, node1, node2, weights):
        
        cnList = self.get_common_neighbors(node1, node2)
        total = 0
        
        for cn in cnList:
            for index in weights:
                total = total + ( self.parameter.get_weights(node1, cn)[index]  + self.parameter.get_weights(node2, cn )[index])
            
        return total
            
        