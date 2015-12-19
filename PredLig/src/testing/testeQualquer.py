'''
Created on Oct 4, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
import networkx
import matplotlib

class Feature(object):
    
    def __init__(self):
        self.graph = None
        self.parameter = None
        
        
    def get_ObjectsofNode(self, graph, mynode):
        return list(edge for n1,n2, edge in  f.graph.edges(data=True) if n1 == mynode or n2 == mynode )
        
    
    
    def getShortestPath(self, node1, node2):
        SPpath = networkx.shortest_path(self.graph, node1,  node2)
        lengthofPath = len(SPpath)
        final =[]
        for index in range(lengthofPath-1):
            final.append([SPpath[index] , SPpath[index+1] ] )
        return final  
    
    def getAllShortestPath(self, node1, node2):
        
        AllPaths = networkx.all_shortest_paths(self.graph, node1,  node2)
        AllCeanPath = []
        for path in AllPaths:
            lengthofPath = len(path)
            final = set()
            for index in range(lengthofPath-1):
                final.add( (path[index] , path[index+1]))
            if final not in AllCeanPath:    
                AllCeanPath.append(final)
        return AllCeanPath  

if __name__ == '__main__':
    result = [0.34,0.23,0.1]
    print sum(result)