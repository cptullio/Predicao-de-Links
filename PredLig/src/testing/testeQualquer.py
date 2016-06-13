'''
Created on 21 de dez de 2015

@author: CarlosPM
'''
import networkx
import matplotlib


if __name__ == '__main__':
    result = []
    
    result.append({'n1':'no1','n2': 'no2', 'aas': 10, 'cn': 1,'jc': 2})
    result.append({'n1':'no1','n2': 'no2', 'aas': 50, 'cn': 5,'jc': 2})
    result.append({'n1':'no1','n2': 'no2', 'aas': 30, 'cn': 56,'jc': 2})
    
    s = sorted(result, key = lambda x: (x['cn']))
    
    print s[len(s)-1]
    print result
    
    
    
    
        
    
        
        
            
   
    
