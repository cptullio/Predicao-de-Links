'''
Created on Jun 16, 2015

@author: cptullio
'''
from featuring.FeatureBase import FeatureBase
import networkx


class LSFeature(FeatureBase):
    '''
    Original Link Score Defined by Chateuar
    '''
    def __repr__(self):
        return 'LS'
    

    def __init__(self):
        super(LSFeature, self).__init__()
        
    
    
    def execute(self, node1, node2):
        
        if not networkx.has_path(self.graph, node1, node2):
            return 0
        total = float(0)
        AllPaths = self.getAllShortestPath(node1, node2)
        SomatorioTPI = float(0)
        for path in AllPaths:
            nodesinPath = set();
            for pairofNodes in path:
                    nodesinPath.add(pairofNodes[0])
                    nodesinPath.add(pairofNodes[1])
                
            print 'Caminho a ser analisado', path
            
            if len(path) <2:
                print "NOT POSSIBLE TO CALCULATED!!  Path Length: " + str(len(path))
                continue
            yearActive = set()
            for node in nodesinPath:
                objectsinNode = self.get_ObjectsofNode(self.graph, node)
                yearActive.add(max(list(x[0] for x in objectsinNode)))
            print 'Active Years', yearActive    
            mediaYear = sum(yearActive)/len(yearActive)
            print 'media Year', mediaYear
            k =  int(self.parameter.t1_)  - mediaYear
            print "k: ", k 
            decay_value = self.parameter.decay ** k
            print "decay value: " , decay_value
            m = len(path)
            sumofPublications = float(0)
            yearsOfPublicationLinks = []
            for pairofNodes in path:
                objectsinLinks = self.get_ObjectsofLinks(self.graph, pairofNodes[0], pairofNodes[1])
                #print "objetos localizados", objectsinLinks
                yearsOfPublicationLinks.append(max(list(x[0] for x in objectsinLinks)))
                sumofPublications = sumofPublications + (1 / float(len(objectsinLinks)))
            hm = m / sumofPublications
            print "Media Harmonica: ", hm
            numeradorTPI = hm * decay_value
            print "Numerador TPI", numeradorTPI
            print "Year of Publications:",  yearsOfPublicationLinks
            denominadorTPI = abs( int(self.parameter.t1_)  - max(yearsOfPublicationLinks )   ) + 1
            print "Denominador TPI", denominadorTPI
            TPI = numeradorTPI / denominadorTPI
            print "TPI: ", TPI 
            
            SomatorioTPI = SomatorioTPI + TPI
            #print "TPI: ", TPI 
            
        TPI_L = SomatorioTPI / float(len(AllPaths)) 
        LINKSCORE = TPI_L /  (len(self.getShortestPath(node1, node2)) -1)
        print "LINK SCORE: ", LINKSCORE    
        return LINKSCORE     
            
        