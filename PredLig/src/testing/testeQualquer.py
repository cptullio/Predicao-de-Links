'''
Created on Dec 19, 2015

@author: cptullio
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse
import networkx

class Teste(object):
    

    def __init__(self,graph):
        self.graph = graph


    def getAllShortestPath(self, node1, node2):
        
        AllPaths = networkx.all_shortest_paths(self.graph, node1,  node2)
        AllCeanPath = []
        for path in AllPaths:
            lengthofPath = len(path)
            final = set()
            for index in range(lengthofPath-1):
                final.add( (path[index] , path[index+1]))
            if final not in AllCeanPath:    
                AllCeanPath.append(final)
        return AllCeanPath            
if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999/AllExecutionScores/configToAG.txt')
    
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    
    myparams.generating_Test_Graph()
    myparams.generating_Training_Graph()
    
    
    selection = VariableSelection(myparams.trainnigGraph, util.min_edges)
    nodesNotLinked = selection.readingResultsFile(util.nodes_notlinked_file)
    calc = CalculateInMemory(myparams,nodesNotLinked)
    resultsofCalculation = calc.executingCalculate()
    #calc.saving_calculateResult(util.calculated_file, resultsofCalculation)
    #calc.saving_calculateResult_normalized(util.calculated_file + '_normalizated.csv', resultsofCalculation)
    #calc.save_Max_min_file(util.maxmincalculated_file, calc.qtyDataCalculated, calc.minValueCalculated, calc.maxValueCalculated)
    #resultsRank = Analyse.AnalyseNodesInFuture(nodesNotLinked, myparams.testGraph)
    #Analyse.saving_analyseResult(resultsRank, util.result_random_file)
    
