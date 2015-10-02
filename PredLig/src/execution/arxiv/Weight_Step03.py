'''
Created on 30 de set de 2015

@author: CarlosPM
'''
from formating.FormatingDataSets import FormatingDataSets
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
from analysing.Analyse import Analyse
from calculating.Calculate import Calculate

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999.txt')
    myparams = Parameterization(util.keyword_decay, util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.generating_Test_Graph()
    calc = Calculate(myparams, util.nodes_file, util.calculated_file + '.weight.txt', util.ordered_file, util.maxmincalculated_file + '.weight.txt')
    #calc.Separating_calculateFile()
    #analise = Analyse(myparams, FormatingDataSets.get_abs_file_path(util.calculated_file + '.weight.txt'), FormatingDataSets.get_abs_file_path(util.analysed_file) + '.random.analised.txt', calc.qtyDataCalculated)
    topRank = Analyse.getTopRank(util.analysed_file + '.random.analised.txt')
    calc.Ordering_separating_File(topRank)
    for OrderingFilePath in calc.getfilePathOrdered_separeted():
        analise = Analyse(myparams, OrderingFilePath, OrderingFilePath + '.analised.txt', topRank )