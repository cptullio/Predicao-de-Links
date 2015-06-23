'''
Created on Jun 21, 2015

@author: cptullio
'''
import unittest
from featuring.FeatureBase import FeatureBase
from parametering.Parameterization import Parameterization
from featuring.CNFeature import CNFeature
from calculating.Calculate import Calculate


class Test(unittest.TestCase):


    def testCalculate(self):
        fb = []
        cn = CNFeature();
        fb.append(cn)
        current_parametration = Parameterization(0, 0, fb, '/Users/cptullio/is_graph.txt')
        print 'Graph ready!'
        calculating = Calculate(current_parametration)
        print 'Graph calculated!'
        
        with open('/Users/cptullio/ai_results.txt', 'w') as fauthorarticleout:
            for r in calculating.results:
                strcalcs = ''
                for c in r.calcs:
                    strcalcs = strcalcs + str(c) +';'  
                fauthorarticleout.write(str(r.node1) + ';' + str(r.node2)+ ';'  +   str(r.current_neighbor_node1)+ ';'  +   str(r.current_neighbor_node2)+ ';'  + strcalcs + '\r\n')
       
        
                   


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCalculate']
    unittest.main()