'''
Created on 8 de jul de 2015

@author: CarlosPM
'''
import unittest
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from formating.dblp.Formating import Formating




class Test(unittest.TestCase):


    
    
    def test_default(self):
        util = ParameterUtil(parameter_file = 'data/parameter.txt')
        print "Formating Graph"
        myDblpFormating = Formating(util.original_file, util.graph_file)
        print "Generating Traning and Testing graphs"
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        analyse = Analyse(myparams, util.calculated_file, util.analysed_file)

    def test_oficial(self):
        util = ParameterUtil('data/pdblp.txt')
        print "Formating Graph"
        print util.original_file, util.graph_file
        myDblpFormating = Formating(util.original_file, util.graph_file)
        print "Generating Traning and Testing graphs"
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
        print "Selecting Nodes not linked"
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        print "Calculating Nodes not linked"
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        print "Analysing results"
        analyse = Analyse(myparams, util.calculated_file, util.analysed_file)

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRunning']
    unittest.main()