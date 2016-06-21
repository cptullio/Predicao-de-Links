'''
Created on 12 de jun de 2016

@author: Administrador
'''
import networkx
import numpy
from formating.arxiv.Formating import Formating

class CalculatingTogetherOnlyNowell(object):
    
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
        TS08 =  len(  list([n1,n2] for n1,n2,result in self.TS08result if result ==1 ) )
        TS05 =  len(  list([n1,n2] for n1,n2,result in self.TS05result if result ==1 ) )
        TS02 =  len(  list([n1,n2] for n1,n2,result in self.TS02result if result ==1 ) )
        
        DTS =  len(  list([n1,n2] for n1,n2,result in self.DTSresult if result ==1 ) )
        return {'aas': AAS, 'cn':CN, 'jc': JC, 'pa': PA, 'ts08': TS08,'ts05': TS05,'ts02': TS02, 'dts': DTS}
    
    
    def AnalyseNodesInFuture(self, ordering, TestGraph):
        self.CNresult = []
        self.AASresult = []
        self.JCresult = []
        self.PAresult = []
        self.TS08result = []
        self.TS05result = []
        self.TS02result = []
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
            
            if (TestGraph.has_edge(nodeToCheck['ts08']['node1'],nodeToCheck['ts08']['node2'])):
                self.TS08result.append([  nodeToCheck['ts08']['node1'],nodeToCheck['ts08']['node2'], 1 ])
            else:
                self.TS08result.append([  nodeToCheck['ts08']['node1'],nodeToCheck['ts08']['node2'], 0 ])
            
            
            if (TestGraph.has_edge(nodeToCheck['ts05']['node1'],nodeToCheck['ts05']['node2'])):
                self.TS05result.append([  nodeToCheck['ts05']['node1'],nodeToCheck['ts05']['node2'], 1 ])
            else:
                self.TS05result.append([  nodeToCheck['ts05']['node1'],nodeToCheck['ts05']['node2'], 0 ])
            
            if (TestGraph.has_edge(nodeToCheck['ts02']['node1'],nodeToCheck['ts02']['node2'])):
                self.TS02result.append([  nodeToCheck['ts02']['node1'],nodeToCheck['ts02']['node2'], 1 ])
            else:
                self.TS02result.append([  nodeToCheck['ts02']['node1'],nodeToCheck['ts02']['node2'], 0 ])
            
            
            
            
            if (TestGraph.has_edge(nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'])):
                self.DTSresult.append([  nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'], 1 ])
            else:
                self.DTSresult.append([  nodeToCheck['dts']['node1'],nodeToCheck['dts']['node2'], 0 ])
            
             
    def normalize(self, data, max, min):
        if min == max:
            return data
        xnormalize = ((data - min)/(max - min))
        return xnormalize
    
    def ordering(self, topRank, normaliza = False):
        orderedResults = []
        
        CN = sorted(self.results, key=lambda value: value['cn'], reverse=True)
        maxCN = CN[0]
        minCN = CN[len(CN)-1]
        AAS = sorted(self.results, key=lambda value: value['aas'], reverse=True)
        maxAAS = AAS[0]
        minAAS = AAS[len(AAS)-1]
        PA = sorted(self.results, key=lambda value: value['pa'], reverse=True)
        maxPA = PA[0]
        minPA = PA[len(PA)-1]
        JC = sorted(self.results, key=lambda value: value['jc'], reverse=True)
        maxJC = JC[0]
        minJC = JC[len(JC)-1]
        TS08 = sorted(self.results, key=lambda value: value['ts08'], reverse=True)
        maxTS08 = TS08[0]
        minTS08 = TS08[len(TS08)-1]
        TS05 = sorted(self.results, key=lambda value: value['ts05'], reverse=True)
        maxTS05 = TS05[0]
        minTS05 = TS05[len(TS05)-1]
        TS02 = sorted(self.results, key=lambda value: value['ts02'], reverse=True)
        maxTS02 = TS02[0]
        minTS02 = TS02[len(TS02)-1]
        
        
        DTS = sorted(self.results, key=lambda value: value['dts'], reverse=True)
        maxDTS = DTS[0]
        minDTS = DTS[len(DTS)-1]
        
        for item in range(topRank):
            #if normaliza:
            #    orderedResults.append({'cn' : self.normalize(CN[item],maxCN,minCN), 'aas':AAS[item], 'pa': PA[item], 'jc':JC[item], 'ts' : TS[item], 'dts' : DTS[item] })
            
           # else:
            orderedResults.append({'cn' : CN[item], 'aas':AAS[item], 'pa': PA[item], 'jc':JC[item], 'ts08' : TS08[item],'ts05' : TS05[item],'ts02' : TS02[item], 'dts' : DTS[item] })
            
    
        return orderedResults
    
    def calculateLS(self, node1, node2, allPaths):
        print node1,node2, allPaths
    
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
            TS_Feature08 = float(0)
            TS_Feature05 = float(0)
            TS_Feature02 = float(0)
            
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
                    hm = 2 / ((1/float(len(objectsNode1))) + (1/float(len(objectsNode2))))
                    timesofLinksNode1 = []
                    timesofLinksNode2 = []
                    bagofWordsNode1 = set()
                    bagofWordsNode2 = set()
            
                    for t1 in objectsNode1:
                        timesofLinksNode1.append(t1['time'])
                    #for bt1 in t1['keywords']:
                    #    bagofWordsNode1.add(bt1)
                    for t2 in objectsNode2:
                        timesofLinksNode2.append(t2['time'])
                    #    for bt2 in t2['keywords']:
                    #        bagofWordsNode2.add(bt2)
            
                    timesofLinksNode1.sort(reverse=True)
                    timesofLinksNode2.sort(reverse=True)
                    timeofLinks = timesofLinksNode1 + timesofLinksNode2
                    k =  int(self.myparams.t0_)  - int(max(timeofLinks))
                    decayfunction08 = (1 - 0.8) ** k
                    decayfunction05 = (1 - 0.5) ** k
                    decayfunction02 = (1 - 0.2) ** k
                    
                    control = (abs( max(timesofLinksNode1) - max(timesofLinksNode2) ) + 1)
                    ts08 = (hm * decayfunction08) / control
                    ts05 = (hm * decayfunction05) / control
                    ts02 = (hm * decayfunction02) / control
                    
                    TS_Feature08 = TS_Feature08 + ts08
                    TS_Feature05 = TS_Feature05 + ts05
                    TS_Feature02 = TS_Feature02 + ts02
                    
                    
                    #dts = (hm * decayfunction) /  (control * ((1 - self.myparams.domain_decay) ** self.get_jacard_domain(bagofWordsNode1, bagofWordsNode2)))
                    #DTS_Feature = DTS_Feature + dts
                
            self.results.append({'node1' : pair[0], 'node2': pair[1], 'cn' : CommonNeigbors_Feature, 'aas' : AAS_Feature, 'jc' : JC_Feature, 'pa' : PA_Feature, 'ts08' : TS_Feature08,'ts05' : TS_Feature05,'ts02' : TS_Feature02, 'dts'  : DTS_Feature })
                
                
        