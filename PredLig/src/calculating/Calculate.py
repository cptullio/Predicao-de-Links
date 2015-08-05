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

class Calculate(object):
	
	
	def reading_calculateFile(self):
		line_values = []
		with open(self.filepathResult) as f:
			content = f.readlines()
			f.close()
		for line in content:
			calcs = []
			cols = line.split('\t')
			for indice in range(len(cols) -2 ):
				calcs.append(float(line.split('\t')[indice].split(':')[1].replace('}','').strip()) )
			line_values.append([calcs, cols[len(cols)-2], cols[len(cols)-1].replace('\n', '')  ] )
		return line_values
	
	
	def printProgressofEvents(self, element, length, message):
		print message, str((float(element)/float(length))*float(100)) + '%', datetime.today()
		
	#after calculating we making the ordering.  This work depends on the quantity of feature
	def orderingCalculate(self):
		print "Starting Ordering the Calculating File", datetime.today()
		all_data_calculated = self.reading_calculateFile()
		if len(self.preparedParameter.featuresChoice) > 1:
			
			justCalculations = []
			for line in all_data_calculated:
				justCalculations.append(line[0])
			inlineArray = set()
			for i in justCalculations:
				for j in i:
					inlineArray.add(j)
			#print inlineArray
			maxvalueofCalculate = max(inlineArray)
			#print justCalculations
			minvalueofCalculate = min(inlineArray)
			mynormalization = []
			result = []
			element = 0
			for itemcalculations in justCalculations:
				#element = element+1
				#self.printProgressofEvents(element, len(justCalculations), "Normalizing Calculations: ")
				newValues = []
				for item in itemcalculations:
					xnormalize = (item - minvalueofCalculate)/(maxvalueofCalculate - minvalueofCalculate)
					#print xnormalize, item, minvalueofCalculate, maxvalueofCalculate
					
					newValues.append(xnormalize)
				mynormalization.append(newValues)
			
			#the result will be the sum of normalizations done, values of each normalization, values before calculate and the pair of nodes.
			element = 0
			qtyCalculatedData = len(all_data_calculated)
			for indice in range(len(all_data_calculated)):
				element = element+1
			
				self.printProgressofEvents(element, qtyCalculatedData , "Sum Normalized Calculations: ")
				result.append( [ numpy.sum(mynormalization[indice]), mynormalization[indice],  all_data_calculated[indice][0], all_data_calculated[indice][1], all_data_calculated[indice][2]  ] )
				
			orderedResult = sorted(result, key=lambda sum_value: sum_value[0], reverse=True)
			
			with open(self.filePathOrdered, 'w') as myfile:
				element = 0
				for item in orderedResult:
					element = element + 1
					self.printProgressofEvents(element, qtyCalculatedData, "Saving data ordered: ")
					myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) +  '\t' +str(item[3]) + '\t' +str(item[4]) +'\r\n')
			
		else:
			orderedResult = sorted(all_data_calculated, key=lambda sum_value: sum_value[0], reverse=True)
			total = len(orderedResult)
			with open(self.filePathOrdered, 'w') as myfile:
				element = 0
				for item in orderedResult:
					element = element + 1
					self.printProgressofEvents(element, total, "Saving data ordered: ")
					myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) +  '\r\n')
		
		print "Ordering the Calculating File finished", datetime.today()
				
		
	
	
	
	def __init__(self, preparedParameter, filepathNodesNotLinked, filepathResult, filePathOrdered):
		print "Starting Calculating Nodes not linked", datetime.today()
		
		self.preparedParameter = preparedParameter
		self.filePathOrdered = Formating.get_abs_file_path(filePathOrdered)
		self.filepathResult = Formating.get_abs_file_path(filepathResult)
		self.filepathNodesNotLinked = Formating.get_abs_file_path(filepathNodesNotLinked)
		#ordering the features by the weight.  Which means that the feature with more weight will appear first.
		featuresOrderedbyScalar = sorted(self.preparedParameter.featuresChoice, key=lambda weigth_value: weigth_value[1], reverse=True)
		self.calculateResults = []
		#for each links that is not linked all the calculates is done.
		element = 0
		qtyofResults = FormatingDataSets.getTotalLineNumbers(self.filepathNodesNotLinked)
		fcontentNodesNotLinked = open(self.filepathNodesNotLinked, 'r')
		fcontentCalcResult = open(self.filepathResult, 'w')
		
		for lineofFile in fcontentNodesNotLinked:
			element = element+1
			self.printProgressofEvents(element, qtyofResults, "Calculating features for nodes not liked: ")
			item = VariableSelection.getItemFromLine(lineofFile)
			
			for neighbor_node in item[1]:
				item_result = []
				#executing the calculation for each features chosen at parameter
				for calc in featuresOrderedbyScalar:
					calc[0].parameter = preparedParameter
					item_result.append(calc[0].execute(item[0],neighbor_node) * calc[1])
					
				final_result = []
				#generating a vetor with the name of the feature and the result of the calculate
				for indice in range(len(featuresOrderedbyScalar)):
					fcontentCalcResult.write( str({str(featuresOrderedbyScalar[indice]):item_result[indice]}) )
					fcontentCalcResult.write('\t')
				fcontentCalcResult.write(str(item[0]) + '\t' + str(neighbor_node)  + '\n'  )
				fcontentCalcResult.flush()
			
		
		fcontentCalcResult.close()
		fcontentNodesNotLinked.close()
		
		print "Calculating Nodes not linked finished", datetime.today()
		
		