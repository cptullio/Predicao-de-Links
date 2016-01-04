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

if __name__ == '__main__':
    
    configFile = 'data/configuration/arxiv/exemplo_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/astroph_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/condmat_1994_1999/MetricaTemporal/config.txt'
    
    resultFile = open(FormatingDataSets.get_abs_file_path(configFile + '.result.txt'), 'w')
    
    util = ParameterUtil(parameter_file = configFile)
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    
    
    myparams.generating_Test_Graph()
    myparams.generating_Training_Graph()
    resultFile.write("TOTAL PAPERS IN TRAINNING: " + str(myparams.get_edges(myparams.trainnigGraph)))
    resultFile.write("\n")
    
    resultFile.write("TOTAL AUTHORS IN TRAINNING: " + str(myparams.get_nodes(myparams.trainnigGraph)))
    resultFile.write("\n")
    
    resultFile.write("TOTAL PAPERS IN TEST: " + str(myparams.get_edges(myparams.testGraph)))
    resultFile.write("\n")
    
    resultFile.write("TOTAL AUTHORS IN TEST: " + str(myparams.get_nodes(myparams.testGraph)))
    resultFile.write("\n")
    
    selection = VariableSelection(myparams.trainnigGraph, util.min_edges)
    nodesNotLinked = selection.get_pair_nodes_not_linked()
    resultFile.write("TOTAL NODES NOT LINKED: " + str(len(nodesNotLinked) ))
    resultFile.write("\n")
    
    selection.saveResults(util.nodes_notlinked_file, nodesNotLinked)
    
    calc = CalculateInMemory(myparams,nodesNotLinked)
    resultsofCalculation = calc.executingCalculate()
    calc.saving_calculateResult(util.calculated_file, resultsofCalculation)
    AnalyseNodesnotLinkedInFuture = Analyse.AnalyseNodesInFuture(nodesNotLinked, myparams.testGraph)
    topRank = Analyse.get_TotalSucess(AnalyseNodesnotLinkedInFuture)
    resultFile.write("TOTAL NODES EFECTIVED LINKED: " + str(topRank) )
    resultFile.write("\n")
    
    Analyse.saving_analyseResult(AnalyseNodesnotLinkedInFuture, util.result_random_file)
    orderingResults = calc.ordering(topRank, resultsofCalculation)
    calc.saving_orderedResult(util.ordered_file, orderingResults)
    ScoresResults = Analyse.AnalyseNodesWithScoresInFuture(orderingResults, myparams.testGraph)
    for index in range(len(ScoresResults)):
        print 'Salving Analysis of ' + str(myparams.ScoresChoiced[index][0] )
        Analyse.saving_analyseResult(ScoresResults[index], util.analysed_file + str(myparams.ScoresChoiced[index][0] ) + '.txt')
        
        resultFile.write("TOTAL OF SUCESSS USING METRIC "  + str(myparams.ScoresChoiced[index][0])  + " = " +  str(Analyse.get_TotalSucess(ScoresResults[index]) ))
                         
        resultFile.write("\n")
        resultFile.write("TOTAL OF FAILED USING METRIC "  + 
                         str(myparams.ScoresChoiced[index][0])  + " = " +  
                         str(Analyse.get_TotalFailed(ScoresResults[index])))  
        resultFile.write("\n")
    resultFile.close()
        
        
        
    