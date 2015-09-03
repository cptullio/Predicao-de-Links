'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx
from datetime import datetime

class TimeScore(FeatureBase):
    '''
    Original TimeScore Defined by Munasigne
    '''
    def __repr__(self):
        return 'ts'
    

    def __init__(self):
        super(TimeScore, self).__init__()
        self.times = {}
        self.debugar = False
        
    def get_TimeofLinks(self, graph, node1, node2):
        result = []
        for node in networkx.common_neighbors(graph, node1, node2):
            if node in self.times:
                if self.debugar:
                    print "already found the time for paper ", node
            else:
                if self.debugar:
                    print "rescuing time from paper: ", str(node)
                
                paper = list(d for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and n == node )
                if self.debugar:
                    print paper[0]['time']
                self.times[node] = paper[0]['time']
            result.append(self.times[node])
        result.sort(reverse=True)
        return result

    
    def execute(self, node1, node2):
        
        
        if node1=='1760' and node2 =='2003':
            self.debugar = True
        else:
            self.debugar = False
        
        pair_common_neighbors  = self.get_common_neighbors(node1, node2)
        if len(pair_common_neighbors) == 0:
            return 0
        if self.debugar:
            print node1, node2, pair_common_neighbors
        timescoreValue = float(0)
        for pair_common_neighbor in pair_common_neighbors:
            timesofLinks = []
            timesofLinksNode1 = self.get_TimeofLinks(self.graph, node1, pair_common_neighbor)
            timesofLinksNode2 = self.get_TimeofLinks(self.graph, node2, pair_common_neighbor)
            
            timesofLinks.append(timesofLinksNode1)
            timesofLinks.append(timesofLinksNode2)
            if self.debugar:
                print node1, pair_common_neighbor, timesofLinksNode1
                print node2, pair_common_neighbor, timesofLinksNode2
            
            
            #Harmonic Mean of Publications
            total = float(0)
            for publications in timesofLinks:
                total = total + 1/float(len(publications))
            hm = 2 / total
            if self.debugar:
                print 'Harmonic meam:', hm
                
            k =  int(self.parameter.t0_)  - int(max(list(timesofLinks))[0])
            decayfunction = (1 - self.parameter.decay) ** k
            control = (abs( max(timesofLinksNode1) - max(timesofLinksNode2) ) + 1)
            ts = (hm * decayfunction) /control
            
            timescoreValue = timescoreValue + ts  
            if self.debugar:
                print 'TS parcial:', timescoreValue
        return timescoreValue    
            
        