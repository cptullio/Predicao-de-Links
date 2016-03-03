'''
Created on Aug 22, 2015

@author: cptullio

First Step is the generation of the graph from the database informations.
We will need the file of parameter to indicate the place where the graph will be saved

'''
from parametering.ParameterUtil import ParameterUtil

from formating.arxiv.Formating import Formating

def step01( paramFile):
    util = ParameterUtil(parameter_file = paramFile)
    astroPh = Formating(util.graph_file)
    astroPh.subject = 'astro-ph'
    astroPh.yearstoRescue = [2009,2010,2011,2012,2013,2014]
    #astroPh.subject = 'cond-mat'
    #astroPh.yearstoRescue = [1994,1995,1996,1997,1998,1999]
    #astroPh.readingOrginalDataset()
    astroPh.generating_graph()
    astroPh.saveGraph()

if __name__ == '__main__':
    step01('data/configuration/arxiv/astroph_2009_2014/MetricaTemporal/config.txt')
    '''
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_condmat_1994_1999.txt')
    astroPh = Formating(util.graph_file)
    astroPh.subject = 'cond-mat'
    astroPh.yearstoRescue = [1994,1995,1996,1997,1998,1999]
    astroPh.readingOrginalDataset()
    #astroPh.generating_graph()
    astroPh.saveGraph()
    '''
    
    
