'''
Created on 12 de ago de 2015

@author: CarlosPM
'''
from datetime import datetime
inicio = datetime.today()
telefones = []


def consultar_cpf(lista_telefone, e):
    print "processa", e,  datetime.today()
    telefones.append(lista_telefone[0])
    
e = 0    
with open('step3_nodesnotlinked_Duarte_ts.txt', 'rb') as arquivo:
    for linha in arquivo:
        e = e +1
        
       
        lista_telefone = []
    
        linhaTexto = linha.strip()
        lista_telefone.append(linhaTexto)
        consultar_cpf(lista_telefone, e)

print len(telefones)
print inicio
print datetime.today()
            