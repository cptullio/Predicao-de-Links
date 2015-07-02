'''
Created on Jul 1, 2015

@author: cptullio
'''
import networkx
import os.path
from formating.dblp.Formating import Formating

class VariableSelection(object):
    '''
    classdocs
    '''
    def get_pair_node_not_linked(self, graph):
        results = []
        group_nodes = set(graph.nodes())
        for node in group_nodes:
            others =   group_nodes - set(networkx.all_neighbors(graph, node))
            others.remove(node)
            for other_node in others:
                isAlreadyThere = 0
                for n in results:
                    if n[0] == node and n[1] == other_node:
                        isAlreadyThere = isAlreadyThere + 1
                    if n[1] == node and n[0] == other_node:
                        isAlreadyThere = isAlreadyThere + 1
                if isAlreadyThere == 0:
                    results.append([node, other_node ])       
        return results
    

    def __init__(self, graph,  filepathNodesToCalculate):
        myfile = Formating.get_abs_file_path(filepathNodesToCalculate)
        if not os.path.exists(myfile):
            self.results = self.get_pair_node_not_linked(graph)
            with open(myfile, 'w') as fnodes:
                for item in self.results:
                    fnodes.write(str(item[0]) + '\t' +  str(item[1]) + '\r\n')
        else:
            self.results = []
            lines = None
            with open(myfile) as f:
                lines = f.readlines()
                f.close()
            for line in lines:
                line = line.strip()
                cols = line.split('\t')
                self.results.append([cols[0], cols[1]])
             
            
        