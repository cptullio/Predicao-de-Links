'''
Created on Aug 22, 2015

@author: cptullio
Analysing the results
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.GenerateWeights import GenerateWeigths

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/configuration/arxiv/grqc_1994_1999/WeightedGraph/config.txt')
    
    #CREATING PARAMETRIZATION OBJECT WITH THE INFORMATIONS OF THE CONFIG FILE.
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    #GENERATING TRAINNING GRAPH BASED ON CONFIG FILE T0 AND T0_
    myparams.generating_Training_Graph()
    #GENERATING TEST GRAPH BASED ON CONFIG FILE T1 AND T1_
    myparams.generating_Test_Graph()
    
    
    AllNodes = VariableSelection(myparams.trainnigGraph, util.nodes_file,util.min_edges, True)
    results = AllNodes.get_all_pair_nodes(myparams.trainnigGraph)
    AllNodes.saveResults(util.nodes_file, results)
    weigths = GenerateWeigths(preparedParameter = myparams, fileAllNodes = util.nodes_file)
    
    
    