'''
Created on Jun 16, 2015

@author: cptullio
'''
from abc import abstractmethod
import networkx as networkx

class FeatureBase(object):
    '''
    Base class for help prepare the features will be used
    '''
    def __init__(self):
        self.graph = None
        self.neighbors_node1 = None
        self.neighbors_node2 = None
        self.parameter = None
    
    def generate_all_node_neighborsfromNode1(self, node1):
        self.neighbors_node1 = set(self.all_node_neighbors(node1))
            
        return self.neighbors_node1
    
    def generate_all_node_neighborsfromNode2(self, node2):
        self.neighbors_node2 = set(self.all_node_neighbors(node2))
        return self.neighbors_node2
       
    @abstractmethod
    def execute(self, node1, node2):
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
    
    
    def get_common_neighbors(self, node1, node2):
        neighbors_node_1 = self.all_node_neighbors(node1)
        neighbors_node_2 = self.all_node_neighbors(node2)
        return neighbors_node_1.intersection(neighbors_node_2)    
    
        
    
