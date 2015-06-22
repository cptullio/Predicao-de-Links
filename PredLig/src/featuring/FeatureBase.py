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
    
    
    def all_node_neighbors(self, node):
        neighbors = set()
        for node_edge in list(networkx.all_neighbors(self.graph, node)):
            for neighbor in list(networkx.all_neighbors(self.graph, node_edge)):
                neighbors.add(neighbor)
        return neighbors - set([node])
    
    def get_pair_node_not_linked(self, group_nodes):
        result = set()
        for node in group_nodes:
            others =   group_nodes - self.all_node_neighbors(node)
            others.remove(node)
            for other_node in others:
                isAlreadyThere = set(n for n in result if (n.first_node == node or n.first_node == other_node) and (n.second_node == node or n.second_node == other_node))
                if len(isAlreadyThere) == 0:
                        result.add(NoLinkedNodes(node, other_node))
        
        return result
         
        
    
        
    
