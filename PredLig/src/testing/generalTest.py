import unittest

import networkx
from formating.dblp.Formating import Formating
import matplotlib
from networkx.classes.function import neighbors
from featuring.CNFeature import CNFeature
from featuring.JCFeature import JCFeature
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from featuring.PAFeature import PAFeature

#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
    
    #First Step of the prcessing:  Formating
    def test_formating(self):
        
        filepathOriginalDataSet = 'data/original/DBLP_Citation_2014_May/domains/ExemploMenor.txt'
        filepathArticleFormatted = 'data/formatado/step1_artile_exemplomenor.txt'
        filepathAuthorFormatted = 'data/formatado/step1_author_exemplomenor.txt'
        filepathArticleAuthorFormatted = 'data/formatado/step1_edge_exemplomenor.txt'
        graphfile = 'data/formatado/step1_graph_exemplomenor.txt'
        myDblpFormating = Formating(filepathOriginalDataSet, filepathArticleFormatted, filepathAuthorFormatted, filepathArticleAuthorFormatted, graphfile)
        #networkx.draw_networkx(myDblpFormating.graph)
        #matplotlib.pyplot.show()
    
    def get_parameter(self):
        filePathGraph = 'data/formatado/step1_graph_exemplomenor.txt'
        t0 = 2000
        t0_ = 2006
        t1 = 2007
        t1_ = 2010
        featuresChoice = []
        cn = CNFeature()
        jc = JCFeature()
        pa = PAFeature()
    
        featuresChoice.append([cn,1])
        featuresChoice.append([jc,1])
        featuresChoice.append([pa,5])
        
        distanceNeighbors = 0
        lengthVertex = 0
        filePathTrainingGraph = 'data/formatado/step2_Traininggraph_exemplomenor.txt'
        filePathTestGraph = 'data/formatado/step2_Testinggraph_exemplomenor.txt'
        myparams = Parameterization(distanceNeighbors, lengthVertex, t0, t0_, t1, t1_, featuresChoice, filePathGraph, filePathTrainingGraph, filePathTestGraph)
        return myparams
    
    def test_parametering(self):
        myparams = self.get_parameter()
        print sorted(myparams.featuresChoice, key=lambda color: color[1], reverse=True)
        
        
        #networkx.draw_networkx(myparams.trainnigGraph)
        #matplotlib.pyplot.show()
    
    #Third Step of the processing: Calculating
    def test_calculating(self):
        #This Step is in fact two steps.  First Variables Select that means which nodes will be processing.
        myparams = self.get_parameter()
        selecting = VariableSelection(myparams.trainnigGraph, 'data/formatado/step3_nodesnotlinked_exemplomenor.txt')
        calc = Calculate(myparams, selecting, 'data/formatado/step3_calc_notOrdered_exemplomenor.txt')   
        print calc.orderedCalculateResult
        
              
                
        
        
        
            
      
        
        
if __name__ == "__main__":
    unittest.main()