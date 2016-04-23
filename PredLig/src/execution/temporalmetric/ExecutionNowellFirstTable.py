'''
Created on 19 de abr de 2016

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from formating.FormatingDataSets import FormatingDataSets

if __name__ == '__main__':
    #configFile = 'data/configuration/arxiv/hepph_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/condmat_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/astroph_1994_1999/MetricaTemporal/config.txt'
    #configFile = 'data/configuration/arxiv/hepth_1994_1999/MetricaTemporal/config.txt'
    configFile = 'data/configuration/arxiv/grqc_1994_1999/MetricaTemporal/config.txt'
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
    collaborations = myparams.get_NowellColaboration()
    eOld = myparams.get_NowellE(nodes,myparams.trainnigGraph)
    print eOld
    eNew = myparams.get_NowellE2(nodes, eOld, myparams.testGraph)
    
    print "Authors\tArticles\tCollaborations\tAuthors\tEold\tEnew"
    print  str(myparams.get_nodes(myparams.trainnigGraph))+ "\t" + str(myparams.get_edges(myparams.trainnigGraph)) + "\t" + str(len(collaborations))+ "\t" + str(len(nodes)) + "\t" + str(len(eOld))+"\t" + str(len(eNew))
        