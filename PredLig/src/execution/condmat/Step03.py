'''
Created on Aug 22, 2015

@author: cptullio
Selecting all Nodes that will be calculated.
'''

from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from formating.FormatingDataSets import FormatingDataSets

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_condmat_1994_1999.txt')
   
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.generating_Training_Graph()
    selection = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    calc = Calculate(myparams, util.nodes_notlinked_file, util.calculated_file, util.ordered_file, util.maxmincalculated_file)
    calc.Separating_calculateFile()
    myparams.generating_Test_Graph()
    #analise = Analyse(myparams, FormatingDataSets.get_abs_file_path(util.calculated_file), FormatingDataSets.get_abs_file_path(util.analysed_file) + '.random.analised.txt', calc.qtyDataCalculated)
    topRank = Analyse.getTopRank(util.analysed_file + '.random.analised.txt')
    calc.Ordering_separating_File(topRank)
    