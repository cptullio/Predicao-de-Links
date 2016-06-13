'''
Created on 12 de jun de 2016

@author: Administrador
'''
import networkx
import numpy
from formating.arxiv.Formating import Formating

class CalculatingTogether(object):
    
    def all_neighbors(self, node):
        return set(networkx.all_neighbors(self.myparams.trainnigGraph, node))
    
    def get_common_neighbors(self, node1, node2):
        neighbors_node_1 = self.all_neighbors(node1)
        neighbors_node_2 = self.all_neighbors(node2)
        return neighbors_node_1.intersection(neighbors_node_2)    
    
    def get_ObjectsofLinks(self, graph, node1, node2):
        T3 = list(edge for n1, n2, edge in graph.edges([node1, node2], data=True) if ((n1 == node1 and n2 == node2) or (n1 == node2 and n2 == node1)) )
        return  T3
    
    def get_jacard_domain(self, bagofWordsNode1, bagofWordsNode2):
        f = (float)(len(bagofWordsNode1.intersection(bagofWordsNode2)))
        x = (float)(len(bagofWordsNode1.union(bagofWordsNode2)))
        if x == 0:
            return 0
        return f/x
    
    
    
    def get_TotalSucess(self):
        
        AAS =  len(  list([n1,n2] for n1,n2,result in self.AASresult if result ==1 ) )
        CN =  len(  list([n1,n2] for n1,n2,result in self.CNresult if result ==1 ) )
        JC =  len(  list([n1,n2] for n1,n2,result in self.JCresult if result ==1 ) )
        PA =  len(  list([n1,n2] for n1,n2,result in self.PAresult if result ==1 ) )
        TS =  len(  list([n1,n2] for n1,n2,result in self.TSresult if result ==1 ) )
        DTS =  len(  list([n1,n2] for n1,n2,result in self.DTSresult if result ==1 ) )
        return {'aas': AAS, 'cn':CN, 'jc': JC, 'pa': PA, 'ts': TS, 'dts': DTS}
    
    
    def AnalyseNodesInFuture(self, ordering, TestGraph):
        self.CNresult = []
        self.AASresult = []
        self.JCresult = []
        self.PAresult = []
        self.TSresult = []
        self.DTSresult = []
        for nodeToCheck in ordering:
            if (TestGraph.has_edge(nodeToCheck['cn']['node1'],nodeToCheck['cn']['node2'])):
                self.CNresult.append([  nodeToCheck['cn']['node1'],nodeToCheck['cn']['node2'], 1 ])
            else:
                self.CNresult.append([  nodeToCheck['cn']['node1'],nodeToCheck['cn']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['aas']['node1'],nodeToCheck['aas']['node2'])):
                self.AASresult.append([  nodeToCheck['aas']['node1'],nodeToCheck['aas']['node2'], 1 ])
            else:
                self.AASresult.append([  nodeToCheck['aas']['node1'],nodeToCheck['aas']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['jc']['node1'],nodeToCheck['jc']['node2'])):
                self.JCresult.append([  nodeToCheck['jc']['node1'],nodeToCheck['jc']['node2'], 1 ])
            else:
                self.JCresult.append([  nodeToCheck['jc']['node1'],nodeToCheck['jc']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['pa']['node1'],nodeToCheck['pa']['node2'])):
                self.PAresult.append([  nodeToCheck['pa']['node1'],nodeToCheck['pa']['node2'], 1 ])
            else:
                self.PAresult.append([  nodeToCheck['pa']['node1'],nodeToCheck['pa']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['ts']['node1'],nodeToCheck['ts']['node2'])):
                self.TSresult.append([  nodeToCheck['ts']['node1'],nodeToCheck['ts']['node2'], 1 ])
            else:
                self.TSresult.append([  nodeToCheck['ts']['node1'],nodeToCheck['ts']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'])):
                self.DTSresult.append([  nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'], 1 ])
            else:
                self.DTSresult.append([  nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'], 0 ])
            
             
    
    
    def ordering(self, topRank):
        orderedResults = []
        
        CN = sorted(self.results, key=lambda value: value['cn'], reverse=True)
        AAS = sorted(self.results, key=lambda value: value['aas'], reverse=True)
        PA = sorted(self.results, key=lambda value: value['pa'], reverse=True)
        JC = sorted(self.results, key=lambda value: value['jc'], reverse=True)
        TS = sorted(self.results, key=lambda value: value['ts'], reverse=True)
        DTS = sorted(self.results, key=lambda value: value['dts'], reverse=True)
        for item in range(topRank):
            orderedResults.append({'cn' : CN[item], 'aas':AAS[item], 'pa': PA[item], 'jc':JC[item], 'ts' : TS[item], 'dts' : DTS[item] })
            
    
        return orderedResults
    
    def __init__(self, myparams, nodesnotlinked):
        self.myparams = myparams
        qtyofNodesToProcess = len(nodesnotlinked)
        element = 0
        self.results = []
        
        for pair in nodesnotlinked:
            element = element+1
            Formating.printProgressofEvents(element, qtyofNodesToProcess, "Calculating features for nodes not liked: ")
            neighbors_node1 = self.all_neighbors(pair[0])
            neighbors_node2 = self.all_neighbors(pair[1])
            CommonNeigbors = neighbors_node1.intersection(neighbors_node2)
            CommonNeigbors_Feature = len(CommonNeigbors)
            AAS_Feature = 0
            JC_Feature = 0
            PA_Feature = len(neighbors_node1) * len(neighbors_node2)
            TS_Feature = float(0)
            DTS_Feature = float(0)
            if CommonNeigbors_Feature > 0:
                print "Calculando ", pair[0], pair[1], CommonNeigbors_Feature
                x = (float)(len(neighbors_node1.union(neighbors_node2)))
                if x > 0:
                    JC_Feature = CommonNeigbors_Feature/x
                for pair_common_neighbor in CommonNeigbors:
                    secondary_neighbors = self.all_neighbors(pair_common_neighbor)
                    AAS_Feature += 1 / (numpy.log10(len(secondary_neighbors)) + 0.00001)
                
                    objectsNode1 = self.get_ObjectsofLinks(myparams.trainnigGraph, pair[0], pair_common_neighbor)
                    objectsNode2 = self.get_ObjectsofLinks(myparams.trainnigGraph, pair[1], pair_common_neighbor)
                    hm = 2 / (1/float(len(objectsNode1))) + (1/float(len(objectsNode2)))
                    timesofLinksNode1 = []
                    timesofLinksNode2 = []
                    bagofWordsNode1 = set()
                    bagofWordsNode2 = set()
            
                    for t1 in objectsNode1:
                        timesofLinksNode1.append(t1['time'])
                    for bt1 in t1['keywords']:
                        bagofWordsNode1.add(bt1)
                    for t2 in objectsNode2:
                        timesofLinksNode2.append(t2['time'])
                        for bt2 in t2['keywords']:
                            bagofWordsNode2.add(bt2)
            
                    timesofLinksNode1.sort(reverse=True)
                    timesofLinksNode2.sort(reverse=True)
                    timeofLinks = timesofLinksNode1 + timesofLinksNode2
                    k =  int(self.myparams.t0_)  - int(max(timeofLinks))
                    decayfunction = (1 - self.myparams.decay) ** k
                    control = (abs( max(timesofLinksNode1) - max(timesofLinksNode2) ) + 1)
                    ts = (hm * decayfunction) / control
                    TS_Feature = TS_Feature + ts
                    dts = (hm * decayfunction) /  (control * ((1 - self.myparams.domain_decay) ** self.get_jacard_domain(bagofWordsNode1, bagofWordsNode2)))
                    DTS_Feature = DTS_Feature + dts
                
                self.results.append({'node1' : pair[0], 'node2': pair[1], 'cn' : CommonNeigbors_Feature, 'aas' : AAS_Feature, 'jc' : JC_Feature, 'pa' : PA_Feature, 'ts' : TS_Feature, 'dts'  : DTS_Feature })
                
                
        