'''
Created on Dec 19, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse
from datetime import datetime

if __name__ == '__main__':
    #util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999/AllExecutionScores/config.txt')
    
    #util = ParameterUtil(parameter_file = 'data/configuration/arxiv/exemplo_1994_1999/CombinationLinear/config.txt')
    #util = ParameterUtil(parameter_file = 'data/configuration/arxiv/condmat_1994_1999/CombinationLinear/config.txt')
    util = ParameterUtil(parameter_file = 'data/configuration/arxiv/astroph_1994_1999/CombinationLinear/config.txt')
    
    
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
    calc.normalizeResultsToCombine(resultsofCalculation)
    calc.saving_calculateResult(util.calculated_file + '_normalizated.csv', resultsofCalculation)
    calc.save_Max_min_file(util.maxmincalculated_file, calc.qtyDataCalculated, calc.minValueCalculated, calc.maxValueCalculated)
    AnalyseNodesnotLinkedInFuture = Analyse.AnalyseNodesInFuture(nodesNotLinked, myparams.testGraph)
    Analyse.saving_analyseResult(AnalyseNodesnotLinkedInFuture, util.result_random_file)
    topRank = Analyse.get_TotalSucess(AnalyseNodesnotLinkedInFuture)
    print 'Total Nodes Not Linked', len(nodesNotLinked)
    print 'Total Success of Nodes Not Linked', topRank
    print 'Total Failed of Nodes Not Linked', Analyse.get_TotalFailed(AnalyseNodesnotLinkedInFuture)
    
    print 'Combinating Metrics', datetime.today()
    resultCombined = calc.combinate_linear(resultsofCalculation)
    print 'Ordering Results of Combinating Metrics', datetime.today()
    OrderedResult = calc.ordering_combinate_linear(topRank, resultCombined)
    
    print 'Analysing Results of Combinating Metrics', datetime.today()
    FinalResult = Analyse.AnalyseNodesInFuture(OrderedResult, myparams.testGraph)
    
    Analyse.saving_analyseResult(FinalResult, util.analysed_file)
    print 'Total Success of Calculated', Analyse.get_TotalSucess(FinalResult)
    print 'Total Failed of Calculated', Analyse.get_TotalFailed(FinalResult)

    
        
