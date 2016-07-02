'''
Created on 19 de abr de 2016

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from formating.FormatingDataSets import FormatingDataSets
import datetime
from calculating.NodeSelection import NodeSelection
from calculating.CalculatingTogetherOnlyNowell import CalculatingTogetherOnlyNowell


def saving_files(filename, data):
    file = open(filename  , 'w')
    file.write(repr(data))
    file.close()
    
def reading_files(filename):
    file = open(filename  , 'r')
    data = eval(file.read())
    return data


def execution(configFile):
    #DEFINE THE FILE THAT WILL KEEP THE RESULT DATA
    resultFile = open(FormatingDataSets.get_abs_file_path(configFile + 'core03.txt'), 'w')
    
    resultFile.write("Inicio da operacao\n")
    resultFile.write(str(datetime.datetime.now()))
    resultFile.write("\n")
    
    #READING THE CONFIG FILE
    util = ParameterUtil(parameter_file = configFile)
    #CREATING PARAMETRIZATION OBJECT WITH THE INFORMATIONS OF THE CONFIG FILE.
    myparams = Parameterization(t0 = util.t0, t0_ = util.t0_, t1 = util.t1, t1_ = util.t1_, linear_combination=util.linear_combination,
                                filePathGraph = util.graph_file, filePathTrainingGraph = util.trainnig_graph_file, filePathTestGraph = util.test_graph_file, decay = util.decay, domain_decay = util.domain_decay, min_edges = util.min_edges, scoreChoiced = util.ScoresChoiced, weightsChoiced = util.WeightsChoiced, weightedScoresChoiced = util.WeightedScoresChoiced, FullGraph = None, result_random_file=util.result_random_file)

    #GENERATING TRAINNING GRAPH BASED ON CONFIG FILE T0 AND T0_
    myparams.generating_Training_Graph()
      
    #GENERATING TEST GRAPH BASED ON CONcvb FIG FILE T1 AND T1_
    myparams.generating_Test_Graph()
    
    nodeSelection = NodeSelection(myparams.trainnigGraph, myparams.testGraph, util)
    

    #CREATING CALCULATION OBJECT
    calc = CalculatingTogetherOnlyNowell(myparams, nodeSelection.nodesNotLinked)

    saving_files(FormatingDataSets.get_abs_file_path(util.calculated_file), calc.results)
    
    Analise = calc.AnalyseAllNodesNotLinkedInFuture(nodeSelection.nodesNotLinked, myparams.testGraph)
    saving_files(FormatingDataSets.get_abs_file_path(util.analysed_file) + '.allNodes.txt', Analise)
    
    resultFile.write("Fim da Operacao\n")
    resultFile.write(str(datetime.datetime.now()))
    
    resultFile.close()

def grqc():
    configFile = 'data/configuration/arxiv/grqc/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def astroph():
    configFile = 'data/configuration/arxiv/astroph/MetricaTemporal/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def condmat():
    configFile = 'data/configuration/arxiv/condmat/MetricaTemporal/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)
    
def hepth():
    configFile = 'data/configuration/arxiv/hepth/MetricaTemporal/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def hepph():
    configFile = 'data/configuration/arxiv/hepph/MetricaTemporal/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

if __name__ == '__main__':
    grqc()
    #astroph()
    #hepth()
    #hepph()
    #condmat()
    
    