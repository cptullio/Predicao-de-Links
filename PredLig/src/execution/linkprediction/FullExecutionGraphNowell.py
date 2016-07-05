'''
Created on 19 de abr de 2016

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from formating.FormatingDataSets import FormatingDataSets
import networkx
import datetime
from calculating.NodeSelection import NodeSelection
from pydblite import Base
import numpy
import os


def saving_files_calculting_input(filename, data):
    
    output = open(filename  , 'w')
    output.write('no1,no2,IntensityNode1,IntensityNode2,Similarity,AgeNo1,AgeNo2\n')
    for item in data:
        output.write(repr(item['no1']))
        output.write(',')
        output.write(repr(item['no2']))
        output.write(',')
        
        output.write(repr(item['intensityno1']))
        output.write(',')
        
        output.write(repr(item['intensityno2']))
        output.write(',')
        
        output.write(repr(item['similarity']))
        output.write(',')
        
        output.write(repr(item['ageno1']))
        output.write(',')
        
        output.write(repr(item['ageno2']))
        output.write('\n')
        
        
    output.close()
    output.close()

def save_file(filename, data):
    
    output = open(filename  , 'w')
    output.write(repr(data))
    output.close()
    


def all_neighbors(graph, node):
    return set(networkx.all_neighbors(graph, node))
    
def get_common_neighbors(graph, node1, node2):
    neighbors_node_1 = all_neighbors(node1)
    neighbors_node_2 = all_neighbors(node2)
    return neighbors_node_1.intersection(neighbors_node_2)    
    
def get_ObjectsofLinks(graph, node1, node2):
    T3 = list(edge for n1, n2, edge in graph.edges([node1, node2], data=True) if ((n1 == node1 and n2 == node2) or (n1 == node2 and n2 == node1)) )
    return  T3
    
def get_jacard_domain(bagofWordsNode1, bagofWordsNode2):
    wN1 = set()
    for n1 in bagofWordsNode1:
        for n11 in n1:
            wN1.add(n11)
    
    wN2 = set()
    for n2 in bagofWordsNode2:
        for n22 in n2:
            wN2.add(n22)
    
       
    f = (float)(len(wN1.intersection(wN2)))
    x = (float)(len(wN1.union(wN2)))
    if x == 0:
        return 0
    return f/x

    

def calculatingInputToFuzzy(graph, nodesnotLinked,  params):
    
    result = []
    element = 0
    qtyofNodesToProcess = len(nodesnotLinked)
    for pair in nodesnotLinked:
        element = element+1
        FormatingDataSets.printProgressofEvents(element, qtyofNodesToProcess, "Calculating features for nodes not liked: ")
        neighbors_node1 = all_neighbors(graph, pair[0])
        neighbors_node2 = all_neighbors(graph, pair[1])
        len_neihbors_node1 = len(neighbors_node1)
        len_neihbors_node2 = len(neighbors_node2)
        CommonNeigbors = neighbors_node1.intersection(neighbors_node2)
        IntensityNode1 = 0;
        IntensityNode2 = 0;
        Similarities = 0;
        Similarity = 0;
        AgesNode1 = 0;
        AgesNode2 = 0;
        
        for cn in CommonNeigbors:
            infoNode1 = list(edge for n1, n2, edge in graph.edges([ pair[0], cn], data=True) if ((n1 ==  pair[0] and n2 == cn) or (n1 == cn and n2 == pair[0])) )
            infoNode2 = list(edge for n1, n2, edge in graph.edges([pair[1], cn], data=True) if ((n1 ==  pair[1] and n2 == cn) or (n1 == cn and n2 == pair[1])) )

            IntensityNode1 = IntensityNode1 + len(infoNode1)
            IntensityNode2 = IntensityNode2 + len(infoNode2)
            
            MaxTimeNode1 =  max(info['time'] for info in infoNode1 if 1==1)
            MaxTimeNode2 =  max(info['time'] for info in infoNode2 if 1==1)

            AgesNode1 = max(AgesNode1,MaxTimeNode1)
            AgesNode2 = max(AgesNode2,MaxTimeNode2)
            
            bagofWordsNode1 =  list(info['keywords'] for info in infoNode1 if 1==1)
            bagofWordsNode2 =  list(info['keywords'] for info in infoNode2 if 1==1)
            
            
            
            Similarities = Similarities + get_jacard_domain(bagofWordsNode1, bagofWordsNode2)
        AgesNode1 = abs(params.t0_ - AgesNode1)    
        AgesNode2 = abs(params.t0_ - AgesNode2)
        if len(CommonNeigbors) > 0:
            Similarity = Similarities / len(CommonNeigbors)
            result.append({ 'no1':  str(pair[0]), 'no2' :str(pair[1]), 'intensityno1' : IntensityNode1,'intensityno2' : IntensityNode2, 'similarity' : Similarity, 'ageno1' :  AgesNode1, 'ageno2' :AgesNode2 })
    return result   
        






    

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
    #if not os.path.exists(FormatingDataSets.get_abs_file_path(util.trainnig_graph_file + '.fuzzyinputy.txt')):
    data = calculatingInputToFuzzy(myparams.trainnigGraph,nodeSelection.nodesNotLinked,  myparams)
    #save_file(FormatingDataSets.get_abs_file_path(util.trainnig_graph_file + '.inputFuzzy.txt'), data)
    saving_files_calculting_input(FormatingDataSets.get_abs_file_path(util.trainnig_graph_file + '.inputFuzzy.txt'), data)
    #else:
    #    db = reading_Database(FormatingDataSets.get_abs_file_path(util.trainnig_graph_file + '.base.pdl'))
    
        
       
    
    resultFile.write("\n")
#        
    resultFile.write("Authors\tArticles\tCollaborations\tAuthors\tEold\tEnew\n")
    resultFile.write( str(myparams.get_nodes(myparams.trainnigGraph))+ "\t" + str(myparams.get_edges(myparams.trainnigGraph)) + "\t\t" + str(len(nodeSelection.get_NowellColaboration())*2)+ "\t\t" + str(len(nodeSelection.nodes)) + "\t" + str(len(nodeSelection.eOld))+"\t" + str(len(nodeSelection.eNeW)))
     
 
    resultFile.write("\n")

    resultFile.write("Fim da Operacao\n")
    resultFile.write(str(datetime.datetime.now()))
    
    resultFile.close()

def grqc():
    #configFile = 'data/configuration/arxiv/grqc/WeightedGraph/config_Arxiv05.txt'
    #configFile = 'data/configuration/arxiv/grqc/WeightedGraph/config_Arxiv99.txt'
    
    configFile = 'data/configuration/arxiv/grqc/LinkPrediction/config_NOWELLTSRich.txt'
    execution(configFile)

def astroph():
    configFile = 'data/configuration/arxiv/astroph/WeightedGraph/config_Arxiv05.txt'
    #configFile = 'data/configuration/arxiv/astroph/WeightedGraph/config_Arxiv99.txt'
    
    #configFile = 'data/configuration/arxiv/astroph/WeightedGraph/config_NOWELLTSRich.txt'
    execution(configFile)

def condmat():
    configFile = 'data/configuration/arxiv/condmat/WeightedGraph/config_Arxiv05.txt'
    #configFile = 'data/configuration/arxiv/condmat/WeightedGraph/config_Arxiv99.txt'
    
    #configFile = 'data/configuration/arxiv/condmat/WeightedGraph/config_NOWELLTSRich.txt'
    execution(configFile)
    
def hepth():
    configFile = 'data/configuration/arxiv/hepth/WeightedGraph/config_Arxiv05.txt'
    #configFile = 'data/configuration/arxiv/hepth/WeightedGraph/config_Arxiv99.txt'
    
    #configFile = 'data/configuration/arxiv/hepth/WeightedGraph/config_NOWELLTSRich.txt'
    execution(configFile)

def hepph():
    configFile = 'data/configuration/arxiv/hepph/WeightedGraph/config_Arxiv05.txt'
    #configFile = 'data/configuration/arxiv/hepph/WeightedGraph/config_Arxiv99.txt'
    
    #configFile = 'data/configuration/arxiv/hepph/WeightedGraph/config_NOWELLTSRich.txt'
    execution(configFile)

if __name__ == '__main__':
    grqc()
    #astroph()
    #hepth()
    #hepph()
    #condmat()
    
    