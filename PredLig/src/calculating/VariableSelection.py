'''
Created on Jul 1, 2015

@author: cptullio
'''
import networkx
import os.path
from formating.dblp.Formating import Formating
from datetime import datetime
from formating.FormatingDataSets import FormatingDataSets
import multiprocessing
import threading
import time


class VariableSelection(object):



    MAX_CONEXOES = 1000

    @staticmethod
    def getItemFromLine(lineofFile):
        cols = lineofFile.strip().replace('\n','').split('\t')
        return [cols[0], eval(cols[1])]
    
    def get_pair_nodes_not_linked(self, graph):
        print "Starting getting pair of nodes that is not liked", datetime.today()
        results = []
        currentNodes =set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
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
        print "getting pair of nodes that is not liked finished", datetime.today()
        
        return results
    

    def cheking_nodes(self,  node1, file):
        others =  set(n for n in self.nodesOrdered if n > node1)
        notLinked = set()
        for other_node in others:
            if len(set(networkx.common_neighbors(self.graph, node1, other_node))) == 0:
                notLinked.add(other_node)
        file.write(str(node1) + '\t' +  repr(notLinked) + '\n')




    def get_pair_nodes_not_linked_saving_in_file(self, graph, file):
        print "Starting getting pair of nodes that is not liked", datetime.today()
        results = []
        currentNodes =set(n for n,d in graph.nodes(data=True) if d['node_type'] == 'N')
        self.nodesOrdered = sorted(currentNodes)
        self.graph = graph
        element = 0
        totalnodesOrdered = len(self.nodesOrdered)
        out_q = multiprocessing.Queue()
        lista_threads = []
        ntreads = 15
        for node1 in self.nodesOrdered:
            element = element+1
            if element % 10 == 0:
                FormatingDataSets.printProgressofEvents(element, totalnodesOrdered, "Checking Node not liked: ")
            
            thread = threading.Thread(target=self.cheking_nodes, args=(node1, file))
            lista_threads.append(thread)
            thread.start()
            if len(lista_threads) > ntreads:
                print "esperando processo"
                for thread in lista_threads:
                    thread.join()
                lista_threads = []
            
        
        
        print "getting pair of nodes that is not liked finished", datetime.today()
        
        



    def __init__(self, graph,  filepathNodesToCalculate):
        myfile = Formating.get_abs_file_path(filepathNodesToCalculate)
        if not os.path.exists(myfile):
            self.results = self.get_pair_nodes_not_linked(graph)
            with open(myfile, 'w') as fnodes:
                self.get_pair_nodes_not_linked_saving_in_file(graph, fnodes)
                fnodes.close()
        else:
            print "Nodes not linked file already generated. please delete if you want a new one.", datetime.today()
                 
            
        