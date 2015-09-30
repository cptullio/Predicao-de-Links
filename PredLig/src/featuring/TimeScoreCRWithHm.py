'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx
from datetime import datetime
import ast

class TimeScoreCRWithHm(FeatureBase):
    '''
    TimeScore modified by Carlos and Ronaldo
    '''
    def __repr__(self):
        return 'tsCRWithHm'
    

    def __init__(self):
        super(TimeScoreCRWithHm, self).__init__()
        
    def get_TimeofLinks(self, graph, node1, node2):
        result = []
        for node in networkx.common_neighbors(graph, node1, node2):
            for n,d in graph.nodes(data=True):
                if n == node:
                    result.append(d['time'])
        result.sort(reverse=True)
        return result
    
    def get_BagofWords(self, graph, node1, node2):
        result = set()
        for node in networkx.common_neighbors(graph, node1, node2):
            for n,d in graph.nodes(data=True):
                if n == node:
                    for keyword in  ast.literal_eval(d['keywords']):
                        result.add(keyword)
                   
        
        return result
    
    def get_jacard_keywords(self, bagofWordsNode1, bagofWordsNode2):
        f = (float)(len(bagofWordsNode1.intersection(bagofWordsNode2)))
        x = (float)(len(bagofWordsNode1.union(bagofWordsNode2)))
        return f/x
    
    def execute(self, node1, node2):
        pair_common_neighbors  = self.get_common_neighbors(node1, node2)
        timesofLinks = []
        timescoreValue = 0
        for pair_common_neighbor in pair_common_neighbors:
            
            timesNode1 = self.get_TimeofLinks(self.graph, node1, pair_common_neighbor)
            timesNode2 = self.get_TimeofLinks(self.graph, node2, pair_common_neighbor)
            print timesNode1
            print timesNode2
            bagofWordsNode1 = self.get_BagofWords(self.graph, node1, pair_common_neighbor)
            bagofWordsNode2 = self.get_BagofWords(self.graph, node2, pair_common_neighbor)
            print bagofWordsNode1
            print bagofWordsNode2
            jcKeyworkds = self.get_jacard_keywords(bagofWordsNode1, bagofWordsNode2)
            print jcKeyworkds
            if jcKeyworkds == 0:
                jcKeyworkds=1;
            print jcKeyworkds
            
            timesofLinks.append(timesNode1)
            timesofLinks.append(timesNode2)
            
            MinNode1 = min(timesNode1)
            MinNode2 = min(timesNode2)
            MaxNode1 = max(timesNode1)
            MaxNode2 = max(timesNode2)
            
            amplitudeMaxima =  abs(min(MinNode1,MinNode2) - int(datetime.today().year))
            frequenciaNode1 = float(len(timesNode1)) / float(amplitudeMaxima)
            frequenciaNode2 = float(len(timesNode2)) / float(amplitudeMaxima)
            
            total = float(0)
            for publications in timesofLinks:
                total = total + 1/float(len(publications))
            hm = 2 / total
            
            
            
            k =  int(datetime.today().year)  - int(max(list(timesofLinks))[0])
            decayfunction = (1 - self.parameter.decay) ** k
            control = (abs( max(list(timesofLinks[0])) - max(list(timesofLinks[1])))  + 1)
            ts =  ( (hm * decayfunction) / control   )
            print ts
            tswithKeywords = ts * (1/jcKeyworkds)
            print tswithKeywords
            timescoreValue = timescoreValue + tswithKeywords
            
        return timescoreValue    
            
        