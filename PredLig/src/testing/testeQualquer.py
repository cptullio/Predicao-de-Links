'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse
from formating.FormatingDataSets import FormatingDataSets
import matplotlib.pyplot as plt
import networkx as nx


if __name__ == '__main__':
    
    configFile = 'data/configuration/arxiv/exemplo_2000_2005/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/cs_2009_2014/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/condmat_2009_2014/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/astroph_2009_2014/MetricaTemporal/config.txt'
    
    
    resultFile = open(FormatingDataSets.get_abs_file_path(configFile + '.result.txt'), 'w')
    
    util = ParameterUtil(parameter_file = configFile)
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    
    
    #
    myparams.generating_Training_Graph()
    myparams.generating_Test_Graph()
    
    
    nx.draw_networkx(myparams.trainnigGraph )  # networkx draw()
    plt.draw()  # pyplot draw()
    plt.show()
    
    nx.draw_networkx(myparams.testGraph)  # networkx draw()
    plt.draw()  # pyplot draw()
    plt.show()
    
