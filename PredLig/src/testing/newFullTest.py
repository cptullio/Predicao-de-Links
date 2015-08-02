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
from formating.duarte.DuarteFormatting import DuarteFormatting

from datetime import datetime



class Test(unittest.TestCase):

    #all type of formatting files will pass through this part of code
    def execute(self, parameter_file):
        util = ParameterUtil(parameter_file = parameter_file)
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
        calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
        calc.orderingCalculate()
        analyse = Analyse(myparams, util.ordered_file, util.analysed_file)

    
    def generate_duarteGeneralData(self):
        util = ParameterUtil(parameter_file = 'data/parameterDuarteBC.txt')
        duarte = DuarteFormatting(util.graph_file)
        duarte.readingOrginalDataset(50)
        duarte.saveGraph()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        print "Selecting Nodes", datetime.today()
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    
    def generate_dblpGeneralData(self, parameter_file):
        util = ParameterUtil(parameter_file)
        format = Formating(util.original_file, util.graph_file)
        format.readingOrginalDataset()
        format.saveGraph()
        myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
        selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    
        
    #do not recomended to run everything direct.  Because the generate take to long time.
    #strong recommended that you comment the lines to run the test step by step
    def test_fullDuarteTest(self):
        self.generate_duarteGeneralData()
        self.execute('data/parameterDuarteTSC.txt')
        self.execute('data/parameterDuarteBC.txt')
    
    def test_fullExemploMenor(self):
        self.generate_dblpGeneralData('data/parameter.txt')
        self.execute('data/parameter.txt')
        self.execute('data/parameter_bc.txt')
    
    def test_dblp(self):
        self.generate_dblpGeneralData('data/pdblp.txt')
        self.execute('data/pdblp.txt')
        self.execute('data/pdblp_bc.txt')
    
  
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRunning']
    unittest.main()