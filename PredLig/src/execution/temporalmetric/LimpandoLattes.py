'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
import networkx
import matplotlib
import os.path
import codecs
import unicodedata
from datetime import datetime
import json

if __name__ == '__main__':
    arquivopath = '/Mestrado-2016/tweets-nov-2012.json/tweets-nov-2012.json.gz.out'
    arquivo = open(arquivopath, 'r')
    
    i=0
    for line in arquivo:
        i=i+1
        print line
        data = json.loads(line)
        
        print data["user_id"]
        #print unicodedata.normalize('NFKD', line)
        
        if i == 100:
            break
            
    #j = json.load(arquivo, encoding='latin-1')
    
    
    
    
    
    
    
    
        
    
            
   
    
