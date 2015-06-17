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
        aas.graph = p.graph
        myedge = p.graph.edges()[0]
        print myedge
        neighbors_node1 = aas.all_neighbors(myedge[0])
        neighbors_node2 = aas.all_neighbors(myedge[1])
        print neighbors_node1
        print neighbors_node2
        print aas.execute(neighbors_node1,neighbors_node2)

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