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
        self.times = {}
        self.debugar = False
        
    def get_TimeofLinks(self, graph, node1, node2):
        result = []
        for node in networkx.common_neighbors(graph, node1, node2):
            if node in self.times:
                if self.debugar:
                    print "already found the time for paper ", node
            else:
                if self.debugar:
                    print "rescuing time from paper: ", str(node)
                
                paper = list(d for n,d in graph.nodes(data=True) if d['node_type'] == 'E' and n == node )
                if self.debugar:
                    print paper[0]['time']
                self.times[node] = paper[0]['time']
            result.append(self.times[node])
        result.sort(reverse=True)
        return result

    
    def execute(self, node1, node2):
        paths = None
        
        try: 
            print "Tentando Pegar o Shotest Path", node1, node2
            
            uniqueShortestPath = list(networkx.shortest_path(self.graph, node1, node2))
            print "Contem Caminho... Pegando todos os Paths", node1, node2
            paths = list(networkx.all_shortest_paths(self.graph, node1, node2))
        except networkx.exception.NetworkXNoPath, e:
            print e
            return 0
    
        AllPaths = []
        for OnePath in paths:
            result = []
            for n in OnePath:
                if not ('P' in n):
                    result.append(n)
            if not result in AllPaths:
                AllPaths.append(result)
        
        print AllPaths
        total = float(0)
        for path in AllPaths:
            
            lengthofPath = len(path)
            final =[]
            for index in range(lengthofPath-1):
                final.append([path[index] , path[index+1] ] )
            
            if len(final) <2:
                print "NOT POSSIBLE TO CALCULATED!!  Path Length: " + str(len(final))
                continue
            yearActive = []
            for nodeinPath in path:
                objectsinNode = self.get_ObjectsofNode(self.graph, nodeinPath)
                yearActive.append(max(list(x[0] for x in objectsinNode)))
            mediaYear = sum(yearActive)/len(yearActive)
            k =  int(self.parameter.t0_)  - mediaYear
            decay_value = self.parameter.decay ** k
            
            m = len(final)
            sumofPublications = float(0)
            yearsOfPublicationLinks = []
            for pairofNodes in final:
                objectsinLinks = self.get_ObjectsofLinks(self.graph, pairofNodes[0], pairofNodes[1])
                #print "objetos localizados", objectsinLinks
                yearsOfPublicationLinks.append(max(list(x[0] for x in objectsinLinks)))
                sumofPublications = sumofPublications + (1 / len(objectsinLinks))
            hm = m / sumofPublications
            numeradorTPI = hm * decay_value
            denominadorTPI = abs( int(self.parameter.t0_)  - max(yearsOfPublicationLinks )   ) + 1
            TPI = numeradorTPI / denominadorTPI
            LinkScore = TPI / ( len(final) - 1)
            total = total + LinkScore 
            
        return total    
            
        