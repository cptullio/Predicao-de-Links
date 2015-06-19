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
       
    @abstractmethod
    def execute(self, neighbor_node1, neighbor_node2):
        raise RuntimeError('not implemented')
    
    def all_neighbors(self, node):
        neighbors = set()
        for neighbor in list(networkx.all_neighbors(self.graph, node)):
            neighbors.add(neighbor)
        return neighbors - set([node])
    
    def has_link(self, neighbor_node1, neighbor_node2):
        neighbors = self.all_neighbors(neighbor_node1)
        for n in neighbors:
            if neighbor_node2 in self.all_neighbors(n):
                return True
                break
        return False
    
    def others(self, node):
        edges = self.all_neighbors(node)
        others_nodes = []
        for n in edges:
            list = self.all_neighbors(n)
            list.remove(node)
            for other in list:
                others_nodes.append(other)
        return others_nodes
    
    def othersWithoutLink(self, node):
        edges = self.all_neighbors(node)
        others_nodes = []
        for n in edges:
            list = self.all_neighbors(n)
            list.remove(node)
            for other in list:
                others_nodes.append(other)
        return others_nodes
        
    
