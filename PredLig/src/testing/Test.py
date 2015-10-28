'''
Created on Oct 4, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
import networkx

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999/config/configuration_forAG.txt')
    
    
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, 
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None)

 
    myparams.generating_Training_Graph()
    paths  = list(networkx.all_simple_paths(myparams.trainnigGraph, '965', '2147'))
    print paths
    
