import unittest

import networkx
from formating.dblp.Formating import Formating
#import matplotlib
from featuring.CNFeature import CNFeature
from featuring.JCFeature import JCFeature
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from featuring.PAFeature import PAFeature
from analysing.Analyse import Analyse

#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
	
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
		featuresChoice.append([jc,4])
		featuresChoice.append([pa,1])
		top_rank = 4
		distanceNeighbors = 0
		lengthVertex = 0
		filePathTrainingGraph = 'data/formatado/step2_Traininggraph_exemplomenor.txt'
		filePathTestGraph = 'data/formatado/step2_Testinggraph_exemplomenor.txt'
		myparams = Parameterization(top_rank, distanceNeighbors, lengthVertex, t0, t0_, t1, t1_, featuresChoice, filePathGraph, filePathTrainingGraph, filePathTestGraph)
		return myparams
    
    
    #First Step of the prcessing:  Formating
	def test_formating(self):
		filepathOriginalDataSet = 'data/original/DBLP_Citation_2014_May/domains/ExemploMenor.txt'
		graphfile = 'data/formatado/step1_graph_exemplomenor.txt'
		myDblpFormating = Formating(filepathOriginalDataSet,  graphfile)
        #networkx.draw_networkx(myDblpFormating.graph)
        #matplotlib.pyplot.show()
    
    #Second Step of processing: Defining the parameters
	def test_parametering(self):
		myparams = self.get_parameter()
        
        #networkx.draw_networkx(myparams.trainnigGraph)
        #matplotlib.pyplot.show()
    
    #Third Step of the processing: Calculating
	def test_calculating(self):
        #This Step is in fact two steps.  First Variables Select that means which nodes will be processing.
		myparams = self.get_parameter()
		selecting = VariableSelection(myparams.trainnigGraph, 'data/formatado/step3_nodesnotlinked_exemplomenor.txt')
        #Second sub-step is calculating the features.
		calc = Calculate(myparams, selecting, 'data/formatado/step3_calculated_exemplomenor.txt')   
        
    #Forth Step of the processing: Calculating
	def test_analysing(self):
		myparams = self.get_parameter()
		analyse = Analyse(myparams, 'data/formatado/step3_calculated_exemplomenor.txt', 'data/formatado/step3_analysed_exemplomenor.txt')
              
        
        
        
if __name__ == "__main__":
    unittest.main()