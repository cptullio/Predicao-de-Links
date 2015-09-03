'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx
from datetime import datetime
import ast

class TimeScoreCR(FeatureBase):
    '''
    TimeScore modified by Carlos and Ronaldo
    '''
    def __repr__(self):
        return 'tsCR'
    

    def __init__(self):
        super(TimeScoreCR, self).__init__()
        self.linkObjects = {}
        
    def get_ObjectsofLinks(self, graph, node1, node2):
        result = []
        for node in networkx.common_neighbors(graph, node1, node2):
            if node in self.linkObjects:
                print "already found the time for paper ", node
            else:
                print "rescuing time from paper: ", str(node)
                
                MaxAmplitude = self.parameter.t0_ - 3
                print MaxAmplitude
                paper = list(d for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and n == node )
                #print paper
                print paper[0]['time']
                if paper[0]['time'] >= MaxAmplitude:
                    self.linkObjects[node] = [paper[0]['time'], eval(paper[0]['keywords'])]
                print self.linkObjects[node]
            result.append(self.linkObjects[node])
            
        #result.sort(reverse=True)
        
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
        if x == 0:
            return 0
        return f/x
    
    def execute(self, node1, node2):
        pair_common_neighbors  = self.get_common_neighbors(node1, node2)
        timesofLinks = []
        timescoreValue = 0
        for pair_common_neighbor in pair_common_neighbors:
            print 'olha!'
            objectsNode1 = self.get_ObjectsofLinks(self.graph, node1, pair_common_neighbor)
            objectsNode2 = self.get_ObjectsofLinks(self.graph, node2, pair_common_neighbor)
            print objectsNode1
            print objectsNode2
            
            timesNode1 = []
            timesNode2 = []
            bagofWordsNode1 = set()
            bagofWordsNode2 = set()
            
            for t1 in objectsNode1:
                timesNode1.append(t1[0])
                for bt1 in t1[1]:
                    bagofWordsNode1.add(bt1)
            for t2 in objectsNode2:
                timesNode2.append(t2[0])
                for bt2 in t2[1]:
                    bagofWordsNode2.add(bt2)
            print timesNode1
            print timesNode2
            print bagofWordsNode1
            print bagofWordsNode2
            jcKeyworkds = self.get_jacard_keywords(bagofWordsNode1, bagofWordsNode2)
            
            timesofLinks.append(timesNode1)
            timesofLinks.append(timesNode2)
            
            MinNode1 = min(timesNode1)
            MinNode2 = min(timesNode2)
            MaxNode1 = max(timesNode1)
            MaxNode2 = max(timesNode2)
            
            total = float(0)
            for publications in timesofLinks:
                total = total + 1/float(len(publications))
            hm = 2 / total
            
            k =  int(self.parameter.t0_)  - int(max(list(timesofLinks))[0])
            decayfunction = (1 - self.parameter.decay) ** k
            control = (abs( max(list(timesofLinks[0])) - max(list(timesofLinks[1])))  + 1)
            ts =  ( (hm * decayfunction) / (control * self.parameter.decay ** jcKeyworkds ) )
            timescoreValue = timescoreValue + ts
            
        return timescoreValue    
            
        