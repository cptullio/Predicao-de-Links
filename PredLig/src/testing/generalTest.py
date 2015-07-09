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
	
	def reading_calculateFile(self, calculated_file):
		myfile = Formating.get_abs_file_path(calculated_file)
		line_values = []
		with open(myfile) as f:
			content = f.readlines()
			f.close()
		for line in content:
			calcs = []
			cols = line.split('\t')
			for indice in range(len(cols) -2 ):
				calcs.append(float(line.split('\t')[indice].split(':')[1].replace('}','').strip()) )
			line_values.append([calcs, cols[len(cols)-2], cols[len(cols)-1].replace('\r\n', '')  ] )
		return line_values
	
	
	def test_readCalculate(self):
		util = ParameterUtil('data/parameter.txt')
		result = []
		for line in self.reading_calculateFile(util.calculated_file):
			calcs = normalize(line[0])
			result.append( [numpy.sum(calcs), calcs, line[0], line[1], line[2]  ] )
		
		orderedResult = sorted(result, key=lambda sum_value: sum_value[0], reverse=True)
		
		for myitem in orderedResult:
			print myitem[0], myitem[1], myitem[2], myitem[3], myitem[4]
		
		
		
		
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