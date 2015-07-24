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
from datetime import datetime



class Test(unittest.TestCase):


    def test_duarte(self):
        util = ParameterUtil(parameter_file = 'data/parameterDuarte.txt')
        print "Generating Traning and Testing graphs", datetime.today()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        print "Selecting Nodes", datetime.today()
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        
        #print "Caculating", datetime.today()
        #calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        #print "Ordering", datetime.today()
        #calc.orderingCalculate()
        #print "Analysing", datetime.today()
        #analyse = Analyse(myparams, util.ordered_file, util.analysed_file)
        
    
    def test_default(self):
        util = ParameterUtil(parameter_file = 'data/parameter.txt')
        print "Formating Graph", datetime.today()
        myDblpFormating = Formating(util.original_file, util.graph_file)
        print "Generating Traning and Testing graphs", datetime.today()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        print "Selecting Nodes", datetime.today()
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        print "Caculating", datetime.today()
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        print "Ordering", datetime.today()
        calc.orderingCalculate()
        print "Analysing", datetime.today()
        analyse = Analyse(myparams, util.ordered_file, util.analysed_file)
    
    def test_timescore(self):
        util = ParameterUtil(parameter_file = 'data/parameter_timescore.txt')
        print "Formating Graph",datetime.today()
        myDblpFormating = Formating(util.original_file, util.graph_file)
        print "Generating Traning and Testing graphs",datetime.today()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        print "Selecting Nodes", datetime.today()
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        print "Caculating", datetime.today()
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        print "Ordering", datetime.today()
        calc.orderingCalculate()
        print "Analysing", datetime.today()
        analyse = Analyse(myparams, util.ordered_file, util.analysed_file)
    
    def test_oficial(self):
        util = ParameterUtil('data/pdblp.txt')
        print "Formating Graph", datetime.today()
        myDblpFormating = Formating(util.original_file, util.graph_file)
        print "Generating Traning and Testing graphs", datetime.today()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file)
        print "Selecting Nodes not linked", datetime.today()
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        print "Calculating Nodes not linked", datetime.today()
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        print "Analysing results", datetime.today()
        analyse = Analyse(myparams, util.calculated_file, util.analysed_file)

        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRunning']
    unittest.main()