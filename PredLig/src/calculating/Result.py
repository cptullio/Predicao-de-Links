'''
Created on Jun 16, 2015

@author: cptullio
'''

class Result(object):
    


    def __init__(self, node1, node2, current_neighbor_node1,current_neighbor_node2, calcs = []):
        self.node1 = node1
        self.node2 = node2
        self.calcs = calcs
        self.current_neighbor_node1 = current_neighbor_node1
        self.current_neighbor_node2 = current_neighbor_node2
        
        
        