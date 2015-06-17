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
    