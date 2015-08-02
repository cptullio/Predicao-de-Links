'''
Created on Jun 14, 2015

@author: cptullio
'''
from abc import abstractmethod
from os import path
import networkx
from datetime import datetime

class FormatingDataSets(object):
    
    @staticmethod
    def get_abs_file_path(relativepath):
        script_path = path.abspath(__file__) 
        script_dir = path.split(script_path)[0]
        return path.join(script_dir, relativepath)
    
    @staticmethod
    def printProgressofEvents(element, length, message):
        print message, str((float(element)/float(length))*float(100)) + '%', datetime.today()
    
    
    @staticmethod
    def reading_graph(relativepath):
        abs_path = FormatingDataSets.get_abs_file_path(relativepath)
        return networkx.read_graphml(abs_path)
    
    def saveGraph(self):
        networkx.write_graphml(self.Graph, self.get_abs_file_path(self.GraphFile)) 
    
    
    @staticmethod
    def get_graph_from_period(graph, t0,t0_):
        print "Starting generating graph from period", datetime.today()
        papers = list([n,d] for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and d['time'] >= t0 and d['time'] <= t0_)
        print "Total Papers: ",  len(papers),  datetime.today()
        new_graph = networkx.Graph()
        new_graph.add_nodes_from(papers)
        element = 0
        for paper in papers:
            element = element+1
            FormatingDataSets.printProgressofEvents(element, len(papers), "Adding paper to new graph: ")
            
            authors = networkx.all_neighbors(graph, paper[0])
            for author in authors:
                author_withData = list([n,d] for n,d in graph.nodes(data=True) if n == author)
                new_graph.add_nodes_from(author_withData)
                new_graph.add_edge(paper[0], author)
        print "Generating graph from period finished", datetime.today()
        return new_graph    
    
    @staticmethod
    def reading_file(abs_file):
        content = None
        with open(abs_file) as f:
            content = f.readlines()
            f.close()
        return content


    @abstractmethod      
    def readingOrginalDataset(self):
        raise RuntimeError('not implemented')
    
    
    def __init__(self, filePathOriginalDataSet, graphfile):
        self.Graph = None
        self.GraphFile = graphfile
        self.OriginalDataSet = self.get_abs_file_path(filePathOriginalDataSet)
        
        