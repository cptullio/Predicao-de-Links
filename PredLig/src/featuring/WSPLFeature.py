'''
Created on Oct 19, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx

class WSPLFeature(FeatureBase):
    '''
    Weighted Shortest Path Length
    Nao possuindo path resultado igual ao total de arestas
    '''
    def __repr__(self):
        return 'SPL'
    

    def __init__(self):
        super(WSPLFeature, self).__init__()
        self.debugar = False
        
    
    
    
    def execute(self, node1, node2, weight_index):
        total = 0
        try:
            
            path = networkx.shortest_path(self.graph, node1,  node2)
            for n in path:
                if not (('P' in n) or (n == node1) or (n == node2)):
                    total = total + ( float(self.parameter.get_weights(node1, n)[int(weight_index)]) +  float(self.parameter.get_weights(node2, n)[int(weight_index)]) )
                     
            return total
        except networkx.exception.NetworkXNoPath, e:
            print 'Error %s' % e
            return self.parameter.getQtyofEdges(self.graph)
        