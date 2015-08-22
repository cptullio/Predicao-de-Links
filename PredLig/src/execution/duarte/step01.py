'''
Created on Aug 22, 2015

@author: cptullio

First Step is the generation of the graph from the database informations.
We will need the file of parameter to indicate the place where the graph will be saved

'''
from parametering.ParameterUtil import ParameterUtil
from formating.duarte.DuarteFormatting import DuarteFormatting

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/duarte/config_muna_justTS.txt')
    duarteFormat = DuarteFormatting(util.graph_file)
    duarteFormat.readingOrginalDataset()
    duarteFormat.saveGraph()
