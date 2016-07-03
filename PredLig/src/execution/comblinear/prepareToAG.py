'''
Created on 19 de abr de 2016

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from formating.FormatingDataSets import FormatingDataSets
import datetime
from calculating.NodeSelection import NodeSelection
from calculating.CalculatingCombinationTogetherOnlyNowell import CalculatingCombinationOnlyNowell


def saving_files_calculting(filename, data):
    
    output = open(filename  , 'w')
    output.write('no1,no2,cn,aas,pa,jc,ts08,ts05,ts02\n')
    for item in data:
        output.write(repr(item['node1']))
        output.write(',')
        output.write(repr(item['node2']))
        output.write(',')
        
        output.write(repr(item['cn']))
        output.write(',')
        
        output.write(repr(item['aas']))
        output.write(',')
        
        output.write(repr(item['pa']))
        output.write(',')
        
        output.write(repr(item['jc']))
        output.write(',')
        
        output.write(repr(item['ts08']))
        output.write(',')
        
        output.write(repr(item['ts05']))
        output.write(',')
        
        output.write(repr(item['ts02']))
        output.write('\n')
        
        
    output.close()
    output.close()

def salvar_analise(filename, data):
    
    output = open(filename, 'w')
    output.write('no1,no2,result\n')
    for item in data:
        output.write(repr(item[0]))
        output.write(',')
        output.write(repr(item[1]))
        output.write(',')
        output.write(repr(item[2]))
        output.write('\n')
                
        
    output.close()
    
        
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
    weights = {'cn' : 1, 'aas': 1, 'pa':1, 'jc': 1, 'ts08':1,'ts05': 1, 'ts02':1}
    
    calc = CalculatingCombinationOnlyNowell(myparams, nodeSelection.nodesNotLinked,weights,False )

    saving_files_calculting(FormatingDataSets.get_abs_file_path(util.calculated_file), calc.results)
    
    Analise = nodeSelection.AnalyseAllNodesNotLinkedInFuture(nodeSelection.nodesNotLinked, myparams.testGraph)
    salvar_analise(FormatingDataSets.get_abs_file_path(util.analysed_file) + '.allNodes.csv', Analise)
    
    resultFile.write("Fim da Operacao\n")
    resultFile.write(str(datetime.datetime.now()))
    
    resultFile.close()

def grqc():
    configFile = 'data/configuration/arxiv/grqc/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def astroph():
    configFile = 'data/configuration/arxiv/astroph/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def condmat():
    configFile = 'data/configuration/arxiv/condmat/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)
    
def hepth():
    configFile = 'data/configuration/arxiv/hepth/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

def hepph():
    configFile = 'data/configuration/arxiv/hepph/CombinationLinear/config_NOWELLTS_BEFOREAG.txt'
    execution(configFile)

if __name__ == '__main__':
    #grqc()
    #astroph()
    #hepth()
    #hepph()
    condmat()
    
    