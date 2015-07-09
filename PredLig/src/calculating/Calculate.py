'''
Created on Jun 16, 2015

@author: cptullio
'''
import networkx
import numpy
from formating.dblp.Formating import Formating

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
			line_values.append([calcs, cols[len(cols)-2], cols[len(cols)-1].replace('\r\n', '')  ] )
		return line_values
	
	def orderingCalculate(self):
		all_data_calculated = self.reading_calculateFile()
		if len(self.preparedParameter.featuresChoice) > 1:
			justCalculations = []
			for line in all_data_calculated:
				justCalculations.append(line[0])
			calculation_mean = numpy.mean(justCalculations)
			calculation_std = numpy.std(justCalculations)
			mynormalization = []
			result = []
			for itemcalculation in justCalculations:
				mynormalization.append([ (itemcalculation[0] - calculation_mean )  / calculation_std, (itemcalculation[1] - calculation_mean )  / calculation_std ])
			for indice in range(len(all_data_calculated)):
				result.append( [ numpy.sum(mynormalization[indice]), mynormalization[indice],  all_data_calculated[indice][0], all_data_calculated[indice][1], all_data_calculated[indice][2]  ] )
		
			orderedResult = sorted(result, key=lambda sum_value: sum_value[0], reverse=True)
			
			with open(self.filePathOrdered, 'w') as myfile:
				for item in orderedResult:
					myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) +  '\t' +str(item[3]) + '\t' +str(item[4]) +'\r\n')
			
		else:
			orderedResult = sorted(all_data_calculated, key=lambda sum_value: sum_value[0], reverse=True)
			
			with open(self.filePathOrdered, 'w') as myfile:
				for item in orderedResult:
					myfile.write(str(item[0]) +  '\t' + str(item[1]) +  '\t' +str(item[2]) +  '\r\n')
		
				
		
	def get_all_author_neighbors(self, graph, current_node):
		authors = set()
		papers = set(networkx.all_neighbors(graph, current_node))
		for paper in papers:
			other_authors =  set(networkx.all_neighbors(graph, paper)) - set(current_node)
			for other in other_authors:
				authors.add(other)
		return authors
	
	
	def __init__(self, preparedParameter, selecting, filepathResult, filePathOrdered):
		self.preparedParameter = preparedParameter
		self.filePathOrdered = Formating.get_abs_file_path(filePathOrdered)
		featuresOrderedbyScalar = sorted(self.preparedParameter.featuresChoice, key=lambda weigth_value: weigth_value[1], reverse=True)
		self.calculateResults = []
		for item in selecting.results:
			neighbors_node1 = set(self.get_all_author_neighbors(self.preparedParameter.trainnigGraph, item[0]))
			neighbors_node2 = set(self.get_all_author_neighbors(self.preparedParameter.trainnigGraph, item[1]))
			item_result = []
			for calc in featuresOrderedbyScalar:
				item_result.append(calc[0].execute(neighbors_node1,neighbors_node2) * calc[1])
			
			final_result = []
			for indice in range(len(featuresOrderedbyScalar)):
				final_result.append({str(featuresOrderedbyScalar[indice]):item_result[indice]} )
			self.calculateResults.append([final_result, item[0], item[1]])
		self.filepathResult = Formating.get_abs_file_path(filepathResult)
		with open(self.filepathResult, 'w') as fnodes:
			for item in self.calculateResults:
				for calc in item[0]:
					fnodes.write(str(calc) + '\t')
				fnodes.write(str(item[1]) +  '\t' +str(item[2]) +'\r\n')
		