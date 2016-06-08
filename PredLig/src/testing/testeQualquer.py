'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
import networkx
import matplotlib


if __name__ == '__main__':
    #arquivoPath = '/grafos/teste.txt'
    arquivoPath = '/Users/Administrador/Downloads/higgs-social_network.edgelist/higgs-social_network.edgelist'
    
        
    arquivo = open(arquivoPath, 'r')
    i = 0
    for line in arquivo:
        i = i+1
        print line 
        if i >100000:  
            break
    
        
        
            
   
    
