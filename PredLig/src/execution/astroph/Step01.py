'''
Created on Aug 22, 2015

@author: cptullio

First Step is the generation of the graph from the database informations.
We will need the file of parameter to indicate the place where the graph will be saved

'''
from parametering.ParameterUtil import ParameterUtil

from formating.arxiv.Formating import Formating

if __name__ == '__main__':
    util = ParameterUtil(parameter_file = 'data/formatado/arxiv/nowell_astroph_1994_1999.txt')
    astroPh = Formating(util.graph_file)
    astroPh.subject = 'astro-ph'
    astroPh.yearstoRescue = [1994,1995,1996,1997,1998,1999]
    astroPh.readingOrginalDataset()
    astroPh.saveGraph()