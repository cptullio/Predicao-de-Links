'''
Created on Aug 22, 2015

@author: cptullio
Analysing the results
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from calculating.VariableSelection import VariableSelection
from formating.FormatingDataSets import FormatingDataSets
import networkx

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_example_3nodes_1994_1999.txt')
    myparams = Parameterization(util.keyword_decay, util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.generating_Training_Graph()
    AllNodes = VariableSelection(myparams.trainnigGraph, util.nodes_file,util.min_edges, True)
    calc = Calculate(myparams, util.nodes_file, util.calculated_file, util.ordered_file, util.maxmincalculated_file)
    
    