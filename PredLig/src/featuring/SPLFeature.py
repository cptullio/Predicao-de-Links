'''
Created on Oct 19, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx

class SPLFeature(FeatureBase):
    '''
    Shortest Path Length
    Nao possuindo path resultado igual a -1
    '''
    def __repr__(self):
        return 'SPL'
    

    def __init__(self):
        super(SPLFeature, self).__init__()
        self.debugar = False
        
    
    
    def execute(self, node1, node2):
        try:
            final = self.getPathLength(node1, node2)
            
            return len(final)
        except networkx.exception.NetworkXNoPath, e:
            print 'Error %s' % e
            return self.parameter.getQtyofEdges(self.graph)
        