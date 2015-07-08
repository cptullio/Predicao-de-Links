'''
Created on Jun 16, 2015

@author: cptullio
'''
import networkx
import numpy
from formating.dblp.Formating import Formating

class Calculate(object):
	
	def normalize(self,arrayToNormalize):
		result = []
		for indice in range(len(arrayToNormalize)):
			std = numpy.std(arrayToNormalize)
			if std == 0:
				result.append(0)
			else:
				vp = arrayToNormalize[indice] - numpy.mean(arrayToNormalize)
				result.append(vp / std)
		return result
	
	def __init__(self, preparedParameter, selecting, filepathResult):
		self.preparedParameter = preparedParameter
		featuresOrderedbyScalar = sorted(self.preparedParameter.featuresChoice, key=lambda color: color[1], reverse=True)
		calculateResults = []
		for item in selecting.results:
			neighbors_node1 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[0]))
			neighbors_node2 = set(networkx.all_neighbors(self.preparedParameter.trainnigGraph, item[1]))
			item_result = []
			for calc in featuresOrderedbyScalar:
				item_result.append(calc[0].execute(neighbors_node1,neighbors_node2) * calc[1])
			normalize_result = item_result #self.normalize(item_result)
			final_result = []
			for indice in range(len(featuresOrderedbyScalar)):
				final_result.append({str(featuresOrderedbyScalar[indice]):normalize_result[indice]} )
			calculateResults.append([final_result, item[0], item[1]])
		myfile = Formating.get_abs_file_path(filepathResult)
		self.orderedCalculateResult = sorted(calculateResults, reverse=True)
		with open(myfile, 'w') as fnodes:
			for item in self.orderedCalculateResult:
				for calc in item[0]:
					fnodes.write(str(calc) + '\t')
				fnodes.write(str(item[1]) +  '\t' +str(item[2]) +'\r\n')
            
        
            
          
            