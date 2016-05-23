'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
import networkx
import matplotlib
import os.path
import codecs

def convert(texto):
    
    dado = texto.replace('\xc3\x80','a')
    dado = dado.replace('\xc3\x81','a')
    dado = dado.replace('\xc3\x82','a')
    dado = dado.replace('\xc3\x83','a')
    dado = dado.replace('\xc3\x84','a')
    dado = dado.replace('\xc3\x85','a')
    dado = dado.replace('\xc3\xa1','a')
    dado = dado.replace('\xc3\xa2','a')
    dado = dado.replace('\xc3\xa3','a')
    dado = dado.replace('\xc3\xa4','a')
    dado = dado.replace('\xc3\xa5','a')
    dado = dado.replace('\xc3\xa6','a')
    dado = dado.replace('\xc3\xa7','cc')
    dado = dado.replace('\xc3\xb3','o')
    dado = dado.replace('\xc3\xb4','o')
    dado = dado.replace('\xc3\xb5','o')
    dado = dado.replace('\xc3\xb6','o')
    dado = dado.replace('\xc3\xb9','u')
    dado = dado.replace('\xc3\xba','u')
    dado = dado.replace('\xc3\xbb','u')
    dado = dado.replace('\xc3\xbc','u')
    dado = dado.replace('\xc3\xa8','e')
    dado = dado.replace('\xc3\xa9','e')
    dado = dado.replace('\xc3\xad','i')
    dado = dado.replace('\xc3\xad','i')
    dado = dado.replace('\xc3\xb1','n')
    dado = dado.replace('-','')
    dado = dado.replace("'",'')
    dado = dado.replace(",",'')
    dado = dado.replace('"','')
    dado = dado.replace('`','')
    dado = dado.replace('\xc4\x8d','vc')
    dado = dado.replace('\xc4\x83','a')
    dado = dado.replace('\xc4\x87','c')
    dado = dado.replace('\xc5\x84','n')
    dado = dado.replace('~','')
    dado = dado.replace('\xc5\x99','vr')
    dado = dado.replace(' Jr.','jr')
    
    return dado

def gerar_grafo(years, graph):
    
    for year in years:
        
        arxivFile = '/grafos/hepth_data.'+ str(year)  + '.txt'
        if os.path.isfile(arxivFile):
            arquivo = open(arxivFile, 'r')
            for line in arquivo:
                cols = line.split('\t')
                if len(cols) == 5:
                    keywords_not_clean = eval(cols[3])
                    keywords = set()
                    for k in keywords_not_clean:
                        keywords.add(k)
                    
                    myVertices = sorted(eval(cols[4]))
                    arxivAutores = []
                    for a in myVertices:
                        #arxivAutores.append(str.upper(a.split(' ')[0][0]) + '_' +  str.upper(convert(a.split(' ')[len(a.split(' '))-1])))
                        arxivAutores.append(a.decode('utf-8'))
                    gerar_dados_grafo(graph, year, str(cols[0]), arxivAutores, keywords)
                       
            
        
    
def gerar_dados_grafo(graph, time, id_edge, autores, keywords):
    myAresta = { 'id_edge': id_edge,  'time' : int(time), 'keywords' : repr(keywords) }
    if len(autores) == 1:
        graph.add_edge(autores[0].strip(), autores[0].strip(),attr_dict=myAresta)
            
    for autor in autores:
        outrosAutores =  set(n for n in autores if n > autor)
        if (len(outrosAutores) == 0):
            graph.add_edge(autor.strip(), autor.strip(),attr_dict=myAresta)
               
        for outro in outrosAutores:
            graph.add_edge(autor.strip(), outro.strip(),attr_dict=myAresta)


def save_nodes(nodes):
    arxivFile = '/grafos/hepth_nodes.txt'
    file = codecs.open(arxivFile,'w', encoding='utf-8')
    for node in nodes:
        file.write(node)
        file.write('\n')
    file.close()
        
        


if __name__ == '__main__':
    
    
    
    graph = networkx.MultiGraph()
    
    gerar_grafo([2010,2011,2012,2013,2014,2015],graph)
    save_nodes(sorted(graph.nodes()))
    
    networkx.write_graphml(graph, '/grafos/hep-th-new-graph.txt') 
    
    
        
    
            
   
    
