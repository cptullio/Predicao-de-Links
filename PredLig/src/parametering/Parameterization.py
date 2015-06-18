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
        self.graph = networkx.Graph()
        with open(self.filePathFormatted) as f:
            self.content = f.readlines()
       
        for line in self.content:
            line = line.strip()
            col = line.split(';')
            node1_id = "Article_%s" %(int(col[0]))
            node2_id = "Author_%s" %(int(col[1]))
            attribute_id = int(col[2])
            self.graph.add_edge(node1_id, node2_id, {'time': attribute_id})
        
        for feature in self.featuresChoice:
            feature.graph = self.graph
        