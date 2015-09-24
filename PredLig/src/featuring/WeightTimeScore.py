'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx
from datetime import datetime
import ast

class WeightTimeScore(FeatureBase):
    '''
    TimeScore modified by Carlos and Ronaldo
    '''
    def __repr__(self):
        return 'WTS'
    

    def __init__(self):
        super(WeightTimeScore, self).__init__()
        self.debugar = False
        
    
    
    
    def execute(self, node1, node2):
        
        papers  = list(networkx.common_neighbors(self.graph, node1, node2))
        if len(papers) == 0:
            return 0
        
        timesofLinks = []
        for paper in papers:
            info_node = list(d for n,d in self.graph.nodes(data=True) if   n == paper )[0]
            timesofLinks.append(int(info_node['time']))
        
               
            
        k =  int(self.parameter.t0_)  - max(timesofLinks)
        decayfunction = (1 - self.parameter.decay) ** k
            
        return decayfunction    
            
        