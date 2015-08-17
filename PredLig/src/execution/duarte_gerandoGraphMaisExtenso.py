'''
Created on Aug 15, 2015

@author: cptullio
'''
from formating.duarte.DuarteFormatting import DuarteFormatting
from parametering.ParameterUtil import ParameterUtil
from parametering.Parameterization import Parameterization
import gc
from calculating.VariableSelection import VariableSelection

if __name__ == '__main__':
    util = ParameterUtil('data/formatado/completo/duarte/config_carlos.txt')
    format = DuarteFormatting( util.graph_file)
    format.readingOrginalDataset()
    format.saveGraph()
    myparams = Parameterization(util.top_rank, util.distanceNeighbors,util.lengthVertex, util.t0, util.t0_, util.t1, util.t1_, util.FeaturesChoiced, util.graph_file, util.trainnig_graph_file, util.test_graph_file, util.decay)
    myparams.generating_Training_Graph()
    selection = VariableSelection(myparams.trainnigGraph, util.nodes_notlinked_file)
    
    