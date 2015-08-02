'''
Created on Aug 2, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from formating.dblp.Formating import Formating
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse



if __name__ == '__main__':
    util = ParameterUtil('data/parameter_dblp_ai_bc.txt')
    format = Formating(util.original_file, util.graph_file)
    format.readingOrginalDataset()
    format.saveGraph()
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    selecting = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    calc = Calculate(myparams, selecting, util.calculated_file, util.ordered_file)
    calc.orderingCalculate()
    analyse = Analyse(myparams, util.ordered_file, util.analysed_file)
