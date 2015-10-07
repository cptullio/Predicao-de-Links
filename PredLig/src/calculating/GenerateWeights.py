'''
Created on Jun 16, 2015

@author: cptullio
'''
import numpy
from formating.dblp.Formating import Formating
from datetime import datetime
from networkx.classes.function import neighbors
from formating.FormatingDataSets import FormatingDataSets
from calculating.VariableSelection import VariableSelection
import os
from _elementtree import Element
import gc
import networkx
import mysql.connector



class GenerateWeigths(object):
    
    
    
    def __init__(self, preparedParameter, fileAllNodes, filepathMaxMinCalculated):
        
        print "Starting Calculating Nodes not linked", datetime.today()
        
        self.preparedParameter = preparedParameter
        
        self.filepathMaxMinCalculated = Formating.get_abs_file_path(filepathMaxMinCalculated)
        self.filepathAllNodes = Formating.get_abs_file_path(fileAllNodes)
        
        self.preparedParameter.open_connection()
        
        element = 0
        qtyLines = FormatingDataSets.getTotalLineNumbers(self.filepathAllNodes)
        
        fcontentAllNodes = open(self.filepathAllNodes, 'r')
        
        self.minValueCalculated = list(99999 for x in self.preparedParameter.featuresChoice)
        self.maxValueCalculated = list(0 for x in self.preparedParameter.featuresChoice)
        
        qtyFeatures = len(self.preparedParameter.WeightFeaturesChoiced)
        qtyNodesCalculated = 0
        partialResults = []
        for lineofFile in fcontentAllNodes:
            element = element+1
            item = VariableSelection.getItemFromLine(lineofFile)
            qtyothernodes = len(item[1])
            newelement = 0
            
            for neighbor_node in item[1]:
                newelement = newelement +1
                qtyNodesCalculated = qtyNodesCalculated + 1
                
                item_result = []
                #executing the calculation for each features chosen at parameter
                for index_features in range(qtyFeatures):
                    self.preparedParameter.WeightFeaturesChoiced[index_features][0].parameter = preparedParameter
                    valueCalculated = self.preparedParameter.featuresChoice[index_features][0].execute(item[0],neighbor_node) * self.preparedParameter.featuresChoice[index_features][1]
                    
                    if valueCalculated < self.minValueCalculated[index_features]:
                        self.minValueCalculated[index_features] = valueCalculated
                    if valueCalculated > self.maxValueCalculated[index_features]:
                        self.maxValueCalculated[index_features] = valueCalculated
                        
                    item_result.append(valueCalculated)
                
                self.preparedParameter.add_weight(item[0], neighbor_node, item_result)
                
                
        
        self.preparedParameter.add_weight(-1,-1, qtyNodesCalculated)
        self.preparedParameter.add_weight(-2,-2, repr(self.minValueCalculated))
        self.preparedParameter.add_weight(-3,-3, repr(self.maxValueCalculated))
            
        print "Calculating Nodes not linked finished", datetime.today()
        
        