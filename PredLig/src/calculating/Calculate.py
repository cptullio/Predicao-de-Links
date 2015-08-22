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


class Calculate(object):
    
    
    def reading_calculateLine(self, line):
        calcs = []
        cols = line.split('\t')
        for indice in range(len(cols) -2 ):
            calcs.append(float(line.split('\t')[indice].split(':')[1].replace('}','').strip()) )
        return [calcs, cols[len(cols)-2], cols[len(cols)-1]  ] 
    
    def normalize(self, data, indice):
        xnormalize = (data - self.minValueCalculated[indice])/(self.maxValueCalculated[indice] - self.minValueCalculated[indice])
        return xnormalize            
        
    def Separating_calculateFile(self):
        self.reading_Max_min_file()
        
        f =  open(self.filepathResult)
        fF = []
        for i in self.preparedParameter.featuresChoice:
            fF.append(open(self.filepathResult +  '.' +str(i) + '.txt', 'w'))
        for line in f:
            calcs = []
            cols = line.split('\t')
            for indice in range(len(cols) -2 ):
                data = float(line.split('\t')[indice].split(':')[1].replace('}','').strip())
                xdata = self.normalize(data, indice)
                fF[indice].write( str(xdata) + ':' + cols[len(cols)-2]  + ':' +  cols[len(cols)-1] )
        f.close()
        for ffF in fF:
            ffF.close()
    
    def reading_Max_min_file(self):
        fcontentMaxMin = open(self.filepathMaxMinCalculated, 'r')
        line = fcontentMaxMin.readline().replace('\n', '')
        data = line.split('\t')
        self.qtyDataCalculated = int(data[0])
        self.minValueCalculated = eval(data[1])
        self.maxValueCalculated = eval(data[2])
        fcontentMaxMin.close()
    
    def getfilePathOrdered_separeted(self):
        data = []
        for indice in range(len(self.preparedParameter.featuresChoice)):
            data.append(self.filePathOrdered +  '.' +str(self.preparedParameter.featuresChoice[indice]) + '.txt')
        return data
    
    def Ordering_separating_File(self):
        print "Starting Ordering the Calculating  in Separating File", datetime.today()
        
        for indice in range(len(self.preparedParameter.featuresChoice)):
            
            fw = open(self.filePathOrdered +  '.' +str(self.preparedParameter.featuresChoice[indice]) + '.txt', 'w')
            
            fr = open(self.filepathResult +  '.' +str(self.preparedParameter.featuresChoice[indice]) + '.txt', 'r')
            data = []
            element = 0
            
            for line in fr:
                element = element + 1
                self.printProgressofEvents(element, self.qtyDataCalculated, "Buffering Calculations to ordering: ")
                
                cols = line.split(':')
                data.append([float(cols[0]), cols[1], cols[2]])
            orderData = sorted(data, key=lambda value: value[0], reverse=True)
            del data
            element = 0
            
            for item in orderData:
                element = element + 1
                self.printProgressofEvents(element, self.qtyDataCalculated, "Saving Data Ordered: ")
                if element == 301:
                    break
                fw.write(str(item[0]) +'\t' + item[1] + '\t' + item[2] )
            del orderData
            fw.close()
            fr.close()
            
            print "Ordering the Calculating  in Separating File FINISHED", datetime.today()
            


    def Ordering__using_memory_separating_File(self):
        print "Starting Ordering the Calculating  in Separating File", datetime.today()
        
        for indice in range(len(self.preparedParameter.featuresChoice)):
            
            fw = open(self.filePathOrdered +  '.' +str(self.preparedParameter.featuresChoice[indice]) + '.txt', 'w')
            
            fr = open(self.filepathResult +  '.' +str(self.preparedParameter.featuresChoice[indice]) + '.txt', 'r')
            print "reading file", str(self.preparedParameter.featuresChoice[indice])
            lines = fr.readlines()
            data = []
            element = 0
            qty = len(lines)
            for line in lines:
                element = element + 1
                if element % 2000 == 0:
                    self.printProgressofEvents(element, qty, "Buffering Calculations to ordering: ")
                
                cols = line.split(':')
                data.append([float(cols[0]), cols[1], cols[2]])
            del lines
            print "ordering file", str(self.preparedParameter.featuresChoice[indice])
            orderData = sorted(data, key=lambda value: value[0], reverse=True)
            element = 0
            for item in orderData:
                element = element + 1
                self.printProgressofEvents(element, self.qtyDataCalculated, "Saving Data Ordered: ")
                if element == 301:
                    break
                fw.write(str(item[0]) +'\t' + item[1] + '\t' + item[2] )
            fw.close()
            fr.close()
            del data
            del orderData
            print "Ordering the Calculating  in Separating File FINISHED", datetime.today()

    
    
    def printProgressofEvents(self, element, length, message):
        print message, str((float(element)/float(length))*float(100)) + '%', datetime.today()

    def printProgressofEventsWihoutPercent(self, element, length, message):
        print message, str(element) + ' of '  +  str(length) , datetime.today()

        
    #after calculating we making the ordering.  This work depends on the quantity of feature
    def orderingCalculate(self):
        print "Starting Ordering the Calculating File", datetime.today()
        
        fResult = open(self.filepathResult, 'r')
        self.reading_Max_min_file()
        result = []
        orderedResult = None
        if len(self.preparedParameter.featuresChoice) > 1:
            element = 0
            for resultLine in fResult:
                element = element+1
                self.printProgressofEvents(element, self.qtyDataCalculated, "Normalizing Calculations: ")
                itemcalculations = self.reading_calculateLine(resultLine)
                
                newValues = []                
                for indice in range(len(itemcalculations[0])):
                    xnormalize =self.normalize(itemcalculations[0][indice], indice)
                    #print xnormalize, item, minvalueofCalculate, maxvalueofCalculate
                    newValues.append(xnormalize)
                
                result.append( [numpy.sum(newValues), newValues, itemcalculations[1],itemcalculations[2]  ] )
                
            orderedResult = sorted(result, key=lambda sum_value: sum_value[0], reverse=True)
            
            with open(self.filePathOrdered, 'w') as myfile:
                element = 0
                for item in orderedResult:
                    element = element + 1
                    self.printProgressofEvents(element, self.qtyDataCalculated, "Saving data ordered: ")
                    myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) +  '\t' +str(item[3]) )
            
        else:
            element = 0
            for resultLine in fResult:
                element = element+1
                self.printProgressofEvents(element, self.qtyDataCalculated, "Reading Calculations: ")
                itemcalculations = self.reading_calculateLine(resultLine)
                result.append( [itemcalculations[0][0], itemcalculations[1],itemcalculations[2]  ] )
            orderedResult = sorted(result, key=lambda sum_value: sum_value[0], reverse=True)
            
            with open(self.filePathOrdered, 'w') as myfile:
                element = 0
                for item in orderedResult:
                    element = element + 1
                    self.printProgressofEvents(element, self.qtyDataCalculated, "Saving data ordered: ")
                    myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) )
        
        print "Ordering the Calculating File finished", datetime.today()
                
        

    
    
    def __init__(self, preparedParameter, filepathNodesNotLinked, filepathResult, filePathOrdered, filepathMaxMinCalculated):
        print "Starting Calculating Nodes not linked", datetime.today()
        
        self.preparedParameter = preparedParameter
        self.filePathOrdered = Formating.get_abs_file_path(filePathOrdered)
        self.filepathMaxMinCalculated = Formating.get_abs_file_path(filepathMaxMinCalculated)
        self.filepathResult = Formating.get_abs_file_path(filepathResult)
        self.filepathNodesNotLinked = Formating.get_abs_file_path(filepathNodesNotLinked)
        #for each links that is not linked all the calculates is done.
        element = 0
        qtyofResults = FormatingDataSets.getTotalLineNumbers(self.filepathNodesNotLinked)
        fcontentNodesNotLinked = open(self.filepathNodesNotLinked, 'r')
        if os.path.exists(self.filepathResult):
            print "Calculate already done for this file, please delete if you want a new one.", datetime.today()
            self.reading_Max_min_file()
            return
        
        fcontentCalcResult = open(self.filepathResult, 'w')
        
        self.minValueCalculated = list(99999 for x in self.preparedParameter.featuresChoice)
        self.maxValueCalculated = list(0 for x in self.preparedParameter.featuresChoice)
        
        qtyFeatures = len(self.preparedParameter.featuresChoice)
        qtyNodesCalculated = 0
        partialResults = []
        for lineofFile in fcontentNodesNotLinked:
            element = element+1
            item = VariableSelection.getItemFromLine(lineofFile)
            qtyothernodenotlinked = len(item[1])
            newelement = 0
            for neighbor_node in item[1]:
                newelement = newelement +1
                qtyNodesCalculated = qtyNodesCalculated + 1
                self.printProgressofEvents(element, qtyofResults, "Calculating features for nodes not liked: ")
                self.printProgressofEventsWihoutPercent(newelement, qtyothernodenotlinked, "Calculating nodes: " + str(item[0])  + ":" +  str(neighbor_node) )
            
                item_result = []
                #executing the calculation for each features chosen at parameter
                for index_features in range(qtyFeatures):
                    self.preparedParameter.featuresChoice[index_features][0].parameter = preparedParameter
                    valueCalculated = self.preparedParameter.featuresChoice[index_features][0].execute(item[0],neighbor_node) * self.preparedParameter.featuresChoice[index_features][1]
                    if valueCalculated < self.minValueCalculated[index_features]:
                        self.minValueCalculated[index_features] = valueCalculated
                    if valueCalculated > self.maxValueCalculated[index_features]:
                        self.maxValueCalculated[index_features] = valueCalculated
                        
                    item_result.append(valueCalculated)
                
                lineContent = []    
                #generating a vetor with the name of the feature and the result of the calculate
                for indice in range(qtyFeatures):
                    lineContent.append(str({str(self.preparedParameter.featuresChoice[indice]):item_result[indice]}) )
                partialResults.append([lineContent, item[0], neighbor_node])
                
            if element % 10 == 0:
                for item in partialResults:
                    for calc in item[0]:
                        fcontentCalcResult.write(calc + '\t')
                    fcontentCalcResult.write(str(item[1]) + '\t' + str(item[2])  + '\n'  )
                partialResults = []
        
        for item in partialResults:
            for calc in item[0]:
                fcontentCalcResult.write(calc + '\t')
            fcontentCalcResult.write(str(item[1]) + '\t' + str(item[2])  + '\n'  )
                
        
        fcontentCalcResult.flush()
        fcontentCalcResult.close()
        fcontentNodesNotLinked.close()
        fcontentMaxMin = open(self.filepathMaxMinCalculated, 'w')
        fcontentMaxMin.write(str(qtyNodesCalculated) + '\t' + repr(self.minValueCalculated) + '\t' + repr(self.maxValueCalculated) )
        fcontentMaxMin.close()
        print "Calculating Nodes not linked finished", datetime.today()
        
        