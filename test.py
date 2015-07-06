import numpy


class MeuTest:
	
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
			
		
	
	def __init__(self):
		meuArray = [1,2,3,44,3,4,0.2,140,0.3]
		print self.normalize(meuArray)
		
		
if __name__ == "__main__":
	meuTest = MeuTest()
	
