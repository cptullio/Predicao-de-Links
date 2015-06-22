'''
Created on Jun 15, 2015

@author: cptullio
'''
import networkx


class Parameterization(object):
    
    def __init__(self, distanceNeighbors, lengthVertex, featuresChoice, filePathFormatted ):
        self.distanceNeighbors = distanceNeighbors
        self.lengthVertex = lengthVertex
        self.featuresChoice = featuresChoice
        self.filePathFormatted = filePathFormatted
        self.graph = networkx.read_graphml(filePathFormatted)
        for feature in self.featuresChoice:
            feature.graph = self.graph
        