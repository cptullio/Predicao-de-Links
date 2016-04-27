'''
Created on 19 de abr de 2016

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from formating.FormatingDataSets import FormatingDataSets
from calculating.CalculateInMemory import CalculateInMemory
from analysing.Analyse import Analyse

if __name__ == '__main__':
    #configFile = 'data/configuration/arxiv/hepph_1994_1999/MetricaTemporal/config.txt'
    configFile = 'data/configuration/arxiv/condmat_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/astroph_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/hepth_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/grqc_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/exemplo_1994_1999/MetricaTemporal/config.txt'
    resultFile = open(FormatingDataSets.get_abs_file_path(configFile + '.firstTable.txt'), 'w')
    util = ParameterUtil(parameter_file = configFile)
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)
    myparams.generating_Training_Graph()
    myparams.generating_Test_Graph()
    
    resultFile.write("TOTAL PAPERS IN TRAINNING: " + str(myparams.get_edges(myparams.trainnigGraph)))
    resultFile.write("\n")
    
    resultFile.write("TOTAL AUTHORS IN TRAINNING: " + str(myparams.get_nodes(myparams.trainnigGraph)))
    resultFile.write("\n")
    nodes = myparams.get_NowellAuthorsCore()
    #print nodes
    collaborations = myparams.get_NowellColaboration()
    #print collaborations
    eOld = myparams.get_NowellE(nodes,myparams.trainnigGraph)
    eNew = myparams.get_NowellE2(nodes, eOld, myparams.testGraph)
    
    print "Authors\tArticles\tCollaborations\tAuthors\tEold\tEnew"
    print  str(myparams.get_nodes(myparams.trainnigGraph))+ "\t" + str(myparams.get_edges(myparams.trainnigGraph)) + "\t\t" + str(len(collaborations))+ "\t\t" + str(len(nodes)) + "\t" + str(len(eOld))+"\t" + str(len(eNew))
        
    #===========================================================================
    # nodesNotLinked = myparams.get_PairsofNodesNotinEold(nodes)
    # calc = CalculateInMemory(myparams,nodesNotLinked)
    # resultsofCalculation = calc.executingCalculate()
    # orderingResults = calc.ordering(len(eNew), resultsofCalculation)
    # calc.saving_orderedResult(util.ordered_file, orderingResults)
    # ScoresResults = Analyse.AnalyseNodesWithScoresInFuture(orderingResults, myparams.testGraph)
    # for index in range(len(ScoresResults)):
    #     print 'Salving Analysis of ' + str(myparams.ScoresChoiced[index][0] )
    #     Analyse.saving_analyseResult(ScoresResults[index], util.analysed_file + str(myparams.ScoresChoiced[index][0] ) + '.txt')
    #    
    #     resultFile.write("TOTAL OF SUCESSS USING METRIC "  + str(myparams.ScoresChoiced[index][0])  + " = " +  str(Analyse.get_TotalSucess(ScoresResults[index]) ))
    #                      
    #     resultFile.write("\n")
    #     resultFile.write("TOTAL OF FAILED USING METRIC "  + 
    #                      str(myparams.ScoresChoiced[index][0])  + " = " +  
    #                      str(Analyse.get_TotalFailed(ScoresResults[index])))  
    #     resultFile.write("\n")
    # resultFile.close()
    #===========================================================================
    
        
    