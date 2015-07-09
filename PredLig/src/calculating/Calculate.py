'''
Created on Jun 16, 2015

@author: cptullio
'''
import networkx
import numpy
from formating.dblp.Formating import Formating

class Calculate(object):
	
	
	
	
	
	def __init__(self, preparedParameter, selecting, filepathResult, filePathOrdered):
		self.preparedParameter = preparedParameter
		self.filePathOrdered = Formating.get_abs_file_path(filePathOrdered)
		featuresOrderedbyScalar = sorted(self.preparedParameter.featuresChoice, key=lambda weigth_value: weigth_value[1], reverse=True)
		self.calculateResults = []
		for item in selecting.results:
			neighbors_node1 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[0]))
			neighbors_node2 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[1]))
			item_result = []
			for calc in featuresOrderedbyScalar:
				item_result.append(calc[0].execute(neighbors_node1,neighbors_node2) * calc[1])
			
			final_result = []
			for indice in range(len(featuresOrderedbyScalar)):
				final_result.append({str(featuresOrderedbyScalar[indice]):item_result[indice]} )
			self.calculateResults.append([final_result, item[0], item[1]])
		myfile = Formating.get_abs_file_path(filepathResult)
		with open(myfile, 'w') as fnodes:
			for item in self.calculateResults:
				for calc in item[0]:
					fnodes.write(str(calc) + '\t')
				fnodes.write(str(item[1]) +  '\t' +str(item[2]) +'\r\n')
		