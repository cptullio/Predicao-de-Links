import unittest

from formating.dblp.Formating import Formating
from parametering.Parameterization import Parameterization
from calculating.VariableSelection import VariableSelection
from calculating.Calculate import Calculate
from analysing.Analyse import Analyse
from parametering.ParameterUtil import ParameterUtil
import networkx
import matplotlib
import numpy
from sklearn.preprocessing import normalize


#python -m unittest GeneralTestings
#export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/"

class GeneralTest(unittest.TestCase):
	
	
	
	
	def test_readCalculate(self):
		util = ParameterUtil('data/parameter.txt')
		f = self.reading_calculateFile(util.calculated_file)
		result = []
		result2 = []
		for line in f:
			result2.append(line[0])
		media = numpy.mean(result2)
		desvio = numpy.std(result2)
		mycalcs = []
		for i in result2:
			mycalcs.append([ (i[0] - media )  / desvio, (i[1] - media )  / desvio ])
		result3 = normalize(result2)
		
		for indice in range(len(f)):
			calcs = normalize(f[indice][0])
			result.append( [ numpy.sum(calcs), numpy.sum(result3[indice]),numpy.sum(mycalcs[indice]), result3[indice], mycalcs[indice] , calcs, f[indice][0], f[indice][1], f[indice][2]  ] )
		
		orderedResult = sorted(result, key=lambda sum_value: sum_value[2], reverse=True)
		
		for myitem in orderedResult:
			print myitem[0], myitem[1], myitem[2], myitem[3], myitem[4], myitem[5], myitem[6], myitem[7], myitem[8]
		
		
		
	def test_viewgraph(self):
		util = ParameterUtil('data/parameter.txt')
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.trainnig_graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.trainnig_graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		networkx.draw_networkx(networkx.read_graphml(Formating.get_abs_file_path(util.test_graph_file)))
		matplotlib.pyplot.savefig(Formating.get_abs_file_path(util.test_graph_file) + ".png", format="PNG")
		matplotlib.pyplot.close()
		
		
		
if __name__ == "__main__":
	unittest.main()