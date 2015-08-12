'''
Created on 12 de ago de 2015

@author: CarlosPM
'''
from datetime import datetime
import multiprocessing

class MyClass(object):
    '''
    classdocs
    '''

    def processar(self, linha, e, dado_saida):
        print "processa", e,  datetime.today()
    
        dado_saida.put(linha)

    def __init__(self, params):
        inicio =  datetime.today()
        out_q = multiprocessing.Queue()
        procs = []
        nprocs = 400
        result = []
        arquivo =  open('step3_nodesnotlinked_Duarte_ts.txt', 'rb')
        elemento = 0;
        for linha in arquivo:
            elemento = elemento + 1
            p = multiprocessing.Process(target=self.processar, args=(linha,elemento, out_q))
            procs.append(p)
            p.start()
            if len(procs) >= nprocs:
                for i in range(len(procs)):
                    result.append(out_q.get())
                
                for p in procs:
                    p.join()
                procs = []
        
        for i in range(len(procs)):
            result.append(out_q.get())
                
        for p in procs:
            p.join()
        
    
        print len(result)
        print inicio
        print datetime.today()
        