'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse

if __name__ == '__main__':
    #util = ParameterUtil(parameter_file = 'data/configuration/arxiv/exemplo_1994_1999/MetricaTemporal/config.txt')
    #util = ParameterUtil(parameter_file = 'data/configuration/arxiv/astroph_1994_1999/MetricaTemporal/config.txt')
    util = ParameterUtil(parameter_file = 'data/configuration/arxiv/condmat_1994_1999/MetricaTemporal/config.txt')
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    
    myparams.generating_Test_Graph()
    myparams.generating_Training_Graph()
    
    selection = VariableSelection(myparams.trainnigGraph, util.min_edges)
    nodesNotLinked = selection.get_pair_nodes_not_linked()
    selection.saveResults(util.nodes_notlinked_file, nodesNotLinked)
    
    calc = CalculateInMemory(myparams,nodesNotLinked)
    resultsofCalculation = calc.executingCalculate()
    calc.saving_calculateResult(util.calculated_file, resultsofCalculation)
    AnalyseNodesnotLinkedInFuture = Analyse.AnalyseNodesInFuture(nodesNotLinked, myparams.testGraph)
    topRank = Analyse.get_TotalSucess(AnalyseNodesnotLinkedInFuture)
    print 'Total ', topRank
    Analyse.saving_analyseResult(AnalyseNodesnotLinkedInFuture, util.result_random_file)
    orderingResults = calc.ordering(topRank, resultsofCalculation)
    calc.saving_orderedResult(util.ordered_file, orderingResults)
    ScoresResults = Analyse.AnalyseNodesWithScoresInFuture(orderingResults, myparams.testGraph)
    Analyse.saving_analyseResult(ScoresResults, util.analysed_file)
    index = 0
    for ScoreResult in ScoresResults:
        
        print  'Metric Result', index, ' = ' ,  Analyse.get_TotalSucess(ScoreResult)
        index = index + 1
        
    