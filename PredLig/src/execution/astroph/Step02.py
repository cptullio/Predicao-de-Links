'''
Created on Aug 22, 2015

@author: cptullio
Process of partition the graph in two for training and for test

'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_2004_2010.txt')
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.generating_Training_Graph()
    myparams.generating_Test_Graph()
    