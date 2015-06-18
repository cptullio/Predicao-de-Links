'''
Created on Jun 15, 2015

@author: cptullio
'''
import unittest
import networkx

from parametering.Parameterization import Parameterization
from featuring.AASFeature import AASFeature
from featuring.JCFeature import JCFeature
from featuring.PAFeature import PAFeature
from calculating.Result import Result
from calculating.Calculate import Calculate
from networkx.classes.graph import Graph
import matplotlib
from featuring.FeatureBase import FeatureBase
from featuring.CNFeature import CNFeature

class Test(unittest.TestCase):

    def testParametrizing(self):
        featuresBase = []
        aas = AASFeature()
        featuresBase.append(aas)
        myfile = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor.txt'
        p = Parameterization(0 , 0, featuresBase , myfile)
        networkx.write_gml(p.graph, '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_graph.gml')
        
               
    def testSecond(self):
        featuresBase = []
        aas = AASFeature()
        featuresBase.append(aas)
        myfile = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor.txt'
        p = Parameterization(0 , 0, featuresBase , myfile)
        myedge = p.graph.edges()[0]
        print myedge
        neighbors_node1 = aas.all_neighbors(myedge[0])
        neighbors_node2 = aas.all_neighbors(myedge[1])
        print neighbors_node1
        print neighbors_node2
        print p.featuresChoice[0].execute(neighbors_node1,neighbors_node2)

    def testThird(self):
        featuresBase = []
        aas = AASFeature()
        featuresBase.append(aas)
        myfile = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor.txt'
        p = Parameterization(0 , 0, featuresBase , myfile)
        print p.graph.nodes()[0]
        print p.graph.nodes()[1]
        myedge = p.graph.nodes()[0]
        neighbors_node1 = aas.all_neighbors(myedge)
        print neighbors_node1
    
    def testGraphCreating(self):
        graph = Graph()
        a1 = 'author_1'
        a2 = 'author_2'
        a3 = 'autor_3'
        p1 = 1
        p2 = 2
        p3 = 3
        graph.add_node(a1, {'time': 0})
        graph.add_node(a2, {'time': 0})
        graph.add_node(a3, {'time': 0})
        graph.add_node(p1, {'time': 1994})
        graph.add_node(p2, {'time': 1996})
        graph.add_node(p3, {'time': 1994})
        
        graph.add_edge(p1,a1)
        graph.add_edge(p1,a2)
        graph.add_edge(p2,a2)
        graph.add_edge(p3,a3)
        
        nodes = set(n for n,d in graph.nodes(data=True) if d['time'] == 0)
        print nodes
        
        
        
        


    def testCalculating(self):
        featuresBase = []
        aas = AASFeature()
        jc = JCFeature()
        pa = PAFeature()
        featuresBase.append(aas)
        featuresBase.append(jc)
        featuresBase.append(pa)
        
        myfile = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor.txt'
        p = Parameterization(0 , 0, featuresBase , myfile)
        calculate = Calculate(p)
        
        myfileResult = '/Users/cptullio/Predicao-de-Links/PredLig/src/data/formatado/dblp_ai_articlearthor_result.txt'
        with open(myfileResult, 'w') as fauthorarticleout:
            for r in calculate.results:
                strcalcs = ''
                for c in r.calcs:
                    strcalcs = strcalcs + str(c) +';'  
                fauthorarticleout.write(str(r.node1) + ';' + str(r.node2)+ ';'  +   str(r.current_neighbor_node1)+ ';'  +   str(r.current_neighbor_node2)+ ';'  + strcalcs + '\r\n')
       

            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()