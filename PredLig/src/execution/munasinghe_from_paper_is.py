'''
Created on 8 de ago de 2015

@author: CarlosPM
'''
from parametering.ParameterUtil import ParameterUtil
from formating.dblp.Formating import Formating
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from datetime import datetime



if __name__ == '__main__':
    util = ParameterUtil('data/formatado/munasinghe/config_frompaper_is.txt')
    #format = Formating(util.original_file, util.graph_file)
    #format.readingOrginalDataset()
    #format.saveGraph()
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    inicio = datetime.today()
    
    selection = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    
    print "Tempo de execucao", (datetime.today() - inicio)
    #calc = Calculate(myparams, util.nodes_notlinked_file, util.calculated_file, util.ordered_file, util.maxmincalculated_file)
    #calc.Separating_calculateFile()
    #analyse = Analyse(myparams, util.ordered_file, util.analysed_file)