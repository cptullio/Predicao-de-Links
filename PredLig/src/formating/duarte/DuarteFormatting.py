'''
Created on Jul 18, 2015

@author: cptullio
'''
import psycopg2
from formating.FormatingDataSets import FormatingDataSets
import networkx


class DuarteFormatting(FormatingDataSets):
    
    
    def __init__(self, graphfile):
        self.Autors = []
        self.Publications = []
        self.AutorsPublicacao = []
        self.GraphFile = graphfile
        self.Graph = None
        super(DuarteFormatting, self).__init__('')
    
        
        
    def saveGraph(self):
        networkx.write_graphml(self.Graph, self.get_abs_file_path(self.GraphFile)) 
        
    
    def generatingGraph(self):
        con = None
        try:
            con = psycopg2.connect(database='projetomestrado', user='postgres', password='123456')
            
            curPublicacao = con.cursor()
            curPublicacao.execute("select idpublicacao, titulo, ano from projetomestrado.publicacao  where ano > 2000 limit 3")
            for linha in curPublicacao.fetchall():
                idpublicacao = linha[0]
                curPublicacaoPalavras = con.cursor()
                curPublicacaoPalavras.execute("select k.keyword from projetomestrado.keyword k inner join projetomestrado.publicacaokeyword pk on pk.idkeyword = k.idkeyword where pk.idpublicacao =" + str(idpublicacao))
                palavras = []
                for palavra in curPublicacaoPalavras.fetchall():
                    palavras.append(palavra[0].strip())
                curAutores = con.cursor()
                curAutores.execute("select a.idautor, a.primeironome, a.ultimonome from projetomestrado.autorpublicacao ap inner join projetomestrado.autor a on a.idautor = ap.idautor where ap.idpublicacao = "+ str(idpublicacao))
                autores = []
                for autor in curAutores.fetchall():
                    autores.append([autor[0], autor[1] + "," + autor[2]])
            
                    
                self.Publications.append([idpublicacao, linha[1], linha[2], palavras, autores ])
            
            graph = networkx.Graph()
            
            
            for item_article in self.Publications:
                graph.add_node('P_' + str(item_article[0]), {'node_type' : 'E', 'title' : item_article[1].decode("latin_1"), 'time' : int(item_article[2]), 'keywords': str(item_article[3]) })
                for item_autor in item_article[4]:
                    graph.add_node(int(item_autor[0]), {'node_type' : 'N', 'name' : item_autor[1].decode("latin_1") })
                    graph.add_edge('P_' + str(item_article[0]), int(item_autor[0]) )
                
            return graph
    
            
            
            
            
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
        finally:
            if con:
                con.close()
    
    
    def readingOrginalDataset(self):
        con = None
        try:
            con = psycopg2.connect(database='projetomestrado', user='postgres', password='123456')
            curAuthor = con.cursor()
            curAuthor.execute("select idautor, ultimonome, primeironome from projetomestrado.autor")
            
            for linha in curAuthor.fetchall():
                self.Autors.append([linha[0], linha[1] + "," + linha[2]])
            
            curPublicacao = con.cursor()
            curPublicacao.execute("select idpublicacao, titulo, ano from projetomestrado.publicacao")
            for linha in curPublicacao.fetchall():
                idpublicacao = linha[0]
                curPublicacaoPalavras = con.cursor()
                curPublicacaoPalavras.execute("select k.keyword from projetomestrado.keyword k inner join projetomestrado.publicacaokeyword pk on pk.idkeyword = k.idkeyword where pk.idpublicacao =" + str(idpublicacao))
                palavras = []
                for palavra in curPublicacaoPalavras.fetchall():
                    palavras.append(palavra[0].strip())
                    
                self.Publications.append([idpublicacao, linha[1], linha[2], palavras ])
            
            curAutorPublicacao = con.cursor()
            curAutorPublicacao.execute(
                                       "select pa.idpublicacao, pa.idautor from projetomestrado.autorpublicacao pa inner join projetomestrado.publicacao p on p.idpublicacao = pa.idpublicacao")
            for linha in curAutorPublicacao.fetchall():
                self.AutorsPublicacao.append([linha[0], linha[1]])
            graph = networkx.Graph()
            print len(self.Autors)    
            
            for item_author in self.Autors:
                graph.add_node(int(item_author[0]), {'node_type' : 'N', 'name' : item_author[1].decode("latin_1") })
            
            print len(self.Publications)    
            
            for item_article in self.Publications:
                graph.add_node('P_' + str(item_article[0]), {'node_type' : 'E', 'title' : item_article[1].decode("latin_1"), 'time' : int(item_article[2]), 'keywords': str(item_article[3]) })
            print len(self.AutorsPublicacao)    
            
            for item_edge in self.AutorsPublicacao:
                graph.add_edge('P_' + str(item_edge[0]), int(item_edge[1]) )
        
            return graph
    
            
            
            
            
        except psycopg2.DatabaseError, e:
            print 'Error %s' % e
        finally:
            if con:
                con.close()
    
        
