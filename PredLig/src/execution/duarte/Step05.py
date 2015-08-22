'''
Created on Aug 22, 2015

@author: cptullio
Ordering Calculation
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.Calculate import Calculate

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/duarte/config_muna_justTS.txt')
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    calc = Calculate(myparams, util.nodes_notlinked_file, util.calculated_file, util.ordered_file, util.maxmincalculated_file)
    calc.Ordering_separating_File()
    