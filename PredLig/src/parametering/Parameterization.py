'''
Created on Jun 15, 2015

@author: cptullio
'''
import networkx
from formating.dblp.Formating import Formating
import os.path


class Parameterization(object):
    
    def __init__(self, distanceNeighbors, lengthVertex, t0, t0_, t1, t1_, featuresChoice, filePathGraph, filePathTrainingGraph, filePathTestGraph):
        self.distanceNeighbors = distanceNeighbors
        self.lengthVertex = lengthVertex
        self.featuresChoice = featuresChoice
        
        self.graph = Formating.reading_graph(filePathGraph)
        if not os.path.exists(Formating.get_abs_file_path(filePathTestGraph)):
            self.testGraph = Formating.get_graph_from_period(self.graph, t1, t1_)
            networkx.write_graphml(self.testGraph, Formating.get_abs_file_path(filePathTestGraph))
        else:
            self.testGraph = Formating.reading_graph(filePathTestGraph)
        if not os.path.exists(Formating.get_abs_file_path(filePathTrainingGraph)):
            self.trainnigGraph = Formating.get_graph_from_period(self.graph, t0, t0_)
            networkx.write_graphml(self.trainnigGraph, Formating.get_abs_file_path(filePathTrainingGraph))
        else:
            self.trainnigGraph = Formating.reading_graph(filePathTrainingGraph)
        
        for feature in self.featuresChoice:
            feature[0].graph = self.trainnigGraph
        