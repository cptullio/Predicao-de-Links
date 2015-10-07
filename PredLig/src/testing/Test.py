'''
Created on Oct 4, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/exemplomenorWeights/nowell_example_1994_1999.txt')
    myparams = Parameterization(util.keyword_decay, util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.open_connection()
    result = [1,3]
    myparams.add_weight(-1 , -1, result)
    myparams.close_mysqlconnection()