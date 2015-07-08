import unittest

from formating.dblp.Formating import Formating
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from parametering.ParameterUtil import ParameterUtil

#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
	
	def get_util(self):
		util = ParameterUtil('data/parameter.txt')
		return util
	
	def get_parameter(self):
		util = self.get_util()
		myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
		return myparams
	
	#First Step of the prcessing:  Formating
	def test_formating(self):
		util = self.get_util()
		myDblpFormating = Formating(util.original_file,  util.graph_file)

	#Second Step of processing: Defining the parameters
	def test_parametering(self):
		myparams = self.get_parameter()
	
	#Third Step of the processing: Calculating
	def test_calculating(self):
		#This Step is in fact two steps.  First Variables Select that means which nodes will be processing.
		util = self.get_util()
		myparams = self.get_parameter()
		selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
		#Second sub-step is calculating the features.
		calc = Calculate(myparams, selecting, util.calculated_file)
	
	#Forth Step of the processing: Calculating
	def test_analysing(self):
		util = self.get_util()
		myparams = self.get_parameter()
		analyse = Analyse(myparams, util.calculated_file, util.analysed_file)

if __name__ == "__main__":
	unittest.main()