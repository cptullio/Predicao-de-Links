'''
Created on Aug 22, 2015

@author: cptullio

First Step is the generation of the graph from the database informations.
We will need the file of parameter to indicate the place where the graph will be saved

'''
from parametering.ParameterUtil import ParameterUtil

from formating.arxiv.Formating import Formating

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/completo/astroph/config_nowell.txt')
    astroPh = Formating(util.graph_file)
    #astroPh.readingOrginalDataset()
    astroPh.generating_graph()
    astroPh.saveGraph()