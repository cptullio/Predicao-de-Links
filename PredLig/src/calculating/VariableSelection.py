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

    @staticmethod
    def getItemFromLine(lineofFile):
        cols = lineofFile.strip().replace('\n','').split('\t')
        return [cols[0], eval(cols[1])]
    
    def get_pair_nodes_not_linked(self, graph, file, min_papers):
        print "Starting getting pair of nodes that is not liked", datetime.today()
        results = []
        nodesinGraph =set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        currentNodes = set()
        for n in nodesinGraph:
            
            papers = set(networkx.all_neighbors(graph, n))
            print papers
            if (len(papers) >= min_papers):
                currentNodes.add(n)
        
        print 'qty of authors: ', len(currentNodes)
        nodesOrdered = sorted(currentNodes)
        element = 0
        totalnodesOrdered = len(nodesOrdered)
        for node1 in nodesOrdered:
            element = element+1
            FormatingDataSets.printProgressofEvents(element, totalnodesOrdered, "Checking Node not liked: ")
            
            others =  set(n for n in nodesOrdered if n > node1)
            notLinked = set()
            for other_node in others:
                if len(set(networkx.common_neighbors(graph, node1, other_node))) == 0:
                    notLinked.add(other_node)
            results.append([node1, notLinked])
            if element % 2000 == 0:
                for item in results:
                    file.write(str(item[0]) + '\t' +  repr(item[1]) + '\n')
                results = []
                
        for item in results:
            file.write(str(item[0]) + '\t' +  repr(item[1]) + '\n')
        results = []
            
        print "getting pair of nodes that is not liked finished", datetime.today()
        
    

    def __init__(self, graph,  filepathNodesToCalculate, min_papers = 1):
        myfile = Formating.get_abs_file_path(filepathNodesToCalculate)
        if not os.path.exists(myfile):
            with open(myfile, 'w') as fnodes:
                self.get_pair_nodes_not_linked(graph,fnodes, min_papers)
                fnodes.close()
        else:
            print "Nodes not linked file already generated. please delete if you want a new one.", datetime.today()
                 
            
        