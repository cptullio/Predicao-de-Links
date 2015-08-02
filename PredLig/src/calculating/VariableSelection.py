'''
Created on Jul 1, 2015

@author: cptullio
'''
import networkx
import os.path
from formating.dblp.Formating import Formating
from datetime import datetime
from formating.FormatingDataSets import FormatingDataSets


class VariableSelection(object):

    
    def get_pair_nodes_not_linked(self, graph):
        print "Starting getting pair of nodes that is not liked", datetime.today()
        results = []
        currentNodes =set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        nodesOrdered = sorted(currentNodes)
        element = 0
        for node1 in nodesOrdered:
            element = element+1
            FormatingDataSets.printProgressofEvents(element, len(nodesOrdered), "Checking Node not liked: ")
            
            others =  set(n for n in nodesOrdered if n > node1)
            for other_node in others:
                if len(set(networkx.common_neighbors(graph, node1, other_node))) == 0:
                    results.append([node1, other_node ])
        print "getting pair of nodes that is not liked finished", datetime.today()
        
        return results
    

    def __init__(self, graph,  filepathNodesToCalculate):
        myfile = Formating.get_abs_file_path(filepathNodesToCalculate)
        if not os.path.exists(myfile):
            self.results = self.get_pair_nodes_not_linked(graph)
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
                line = line.replace('\r\n','')
                line = line.strip()
                cols = line.split('\t')
                self.results.append([cols[0], cols[1]])
             
            
        