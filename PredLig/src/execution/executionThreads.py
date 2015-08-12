'''
Created on 12 de ago de 2015

@author: CarlosPM
'''

import threading
import time
import sys,os
import subprocess
from datetime import datetime
 

MAX_CONEXOES = 100000

global telefones

print datetime.today()

telefones = []
 
 
print_lock = threading.Lock()
def mostrar_msg(msg):
    print_lock.acquire()
    print msg
    print_lock.release()
 
def consultar_cpf(lista_telefone):
    #print "consultando CPF \n"
    telefones.append(lista_telefone[0])
    #if len(telefones) == 10:
    #    print telefones
    #    print "\n\n\n\n\n"
    #print "fim da Consulta CPF \n"
    
    
 
lista_threads = []
contador = 1
with open('step3_nodesnotlinked_Duarte_ts.txt', 'rb') as arquivo:
    for linha in arquivo:
        
            linhaTexto = linha.strip()
            lista_telefone.append(linhaTexto)
            while threading.active_count() > MAX_CONEXOES:
                #mostrar_msg("Esperando 2s...")
                time.sleep(1)
            thread = threading.Thread(target=consultar_cpf, args=(lista_telefone,))
            lista_threads.append(thread)
            thread.start()
            contador =+ 1
        elif contador == 100000:
            contador = 1
            
 
mostrar_msg("Esperando threads abertas terminarem...")
for thread in lista_threads:
    thread.join()
print len(telefones)
print datetime.today()

