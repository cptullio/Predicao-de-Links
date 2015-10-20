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
        total = 0
        try:
            path = networkx.shortest_path(self.graph, node1,  node2)
            for n in path:
                if not (('P' in n) or (n == node1) or (n == node2)):
                    total = total + 1
            return self.parameter.decay ** total
        except networkx.exception.NetworkXNoPath, e:
            print 'Error %s' % e
            return 0
        