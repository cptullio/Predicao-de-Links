'''
Created on Jun 16, 2015

@author: cptullio
'''
from abc import abstractmethod
import networkx as networkx

class NoLinkedNodes(object):
    def __init__(self, first_node, second_node):
        self.first_node = first_node
        self.second_node = second_node
    

class FeatureBase(object):
    '''
    Base class for help prepare the features will be used
    '''
    def __init__(self):
        self.graph = None
       
    @abstractmethod
    def execute(self, neighbor_node1, neighbor_node2):
        raise RuntimeError('not implemented')
    
    def all_neighbors(self, node):
        neighbors = set()
        for neighbor in list(networkx.all_neighbors(self.graph, node)):
            neighbors.add(neighbor)
        return neighbors - set([node])
    
    #from graph where the edge is define by other type of node
    def all_node_neighbors(self, node):
        neighbors = set()
        for node_edge in list(networkx.all_neighbors(self.graph, node)):
            for neighbor in list(networkx.all_neighbors(self.graph, node_edge)):
                neighbors.add(neighbor)
        return neighbors - set([node])
    
         
        
    
        
    
