'''
Created on Oct 4, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/exemplomenorWeights/nowell_example_1994_1999.txt')
    myparams = Parameterization(keyword_decay= util.keyword_decay, lengthVertex = util.lengthVertex, t0 = util.t0, t0_ = util.t0_ , t1 = util.t1, t1_ = util.t1_, featuresChoice = util.FeaturesChoiced, filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, FullGraph = None, min_edges = util.min_edges, weightFeaturesChoiced = util.WeightFeaturesChoiced, featuresusingWeightsChoiced= util.FeaturesForWeightChoiced)
    
    print len(myparams.featuresusingWeightsChoiced)
    