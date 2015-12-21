'''
Created on Dec 19, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse
import datetime

if __name__ == '__main__':
    #util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999/AllExecutionScores/config.txt')
    util = ParameterUtil(parameter_file = 'data/configuration/arxiv/exemplo_1994_1999/CombinationLinear/config.txt')
    
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    
    myparams.generating_Test_Graph()
    myparams.generating_Training_Graph()
    selection = VariableSelection(myparams.trainnigGraph, util.min_edges)
    nodesNotLinked = selection.readingResultsFile(util.nodes_notlinked_file)
    
    calc = CalculateInMemory(myparams,nodesNotLinked)
    resultsNormalized = calc.reading_calculateResult_normalized(util.calculated_file + '_normalizated.csv')
    AnalyseNodesnotLinkedInFuture = Analyse.reading_analyseResult(util.result_random_file)
    topRank = Analyse.get_TotalSucess(AnalyseNodesnotLinkedInFuture)
    print 'Total Nodes Not Linked', len(nodesNotLinked)
    print 'Total Success of Nodes Not Linked', topRank
    print 'Total Failed of Nodes Not Linked', Analyse.get_TotalFailed(AnalyseNodesnotLinkedInFuture)
    
    print 'Combinating Metrics', datetime.datetime.today()
    resultCombined = calc.combinate_linear(resultsNormalized)
    print 'Ordering Results of Combinating Metrics', datetime.datetime.today()
    OrderedResult = calc.ordering_combinate_linear(topRank, resultCombined)
    
    print 'Analysing Results of Combinating Metrics', datetime.datetime.today()
    FinalResult = Analyse.AnalyseNodesInFuture(OrderedResult, myparams.testGraph)
    
    Analyse.saving_analyseResult(FinalResult, util.analysed_file)
    print 'Total Success of Calculated', Analyse.get_TotalSucess(FinalResult)
    print 'Total Failed of Calculated', Analyse.get_TotalFailed(FinalResult)
    
    
