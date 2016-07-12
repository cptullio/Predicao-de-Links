'''
Created on 12 de jun de 2016

@author: Administrador
'''
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

class FuzzyCalculation(object):
    
        
    
    def __init__(self, intensidade_interacoes_AC, intensidade_interacoes_BC, similaridade_entre_vertices, idade_interacoes_AC, idade_interacoes_BC, ShowGraphics = False):
        print intensidade_interacoes_AC, intensidade_interacoes_BC, similaridade_entre_vertices, idade_interacoes_AC,idade_interacoes_BC
        self.intensidade_interacoes_AC = intensidade_interacoes_AC
        self.intensidade_interacoes_BC = intensidade_interacoes_BC
        self.similaridade_entre_vertices = similaridade_entre_vertices
        self.idade_interacoes_AC = idade_interacoes_AC
        self.idade_interacoes_BC = idade_interacoes_BC
        
        # Generate universe variables
        self.x_intensidade_interacoes_AC   = np.arange(0, 100, 1)
        self.x_intensidade_interacoes_BC   = np.arange(0, 100, 1)
        self.x_similaridade_entre_vertices = np.arange(0, 101, 1)
        self.x_idade_interacoes_AC         = np.arange(0, 10, 1)
        self.x_idade_interacoes_BC         = np.arange(0, 10, 1)
        self.x_potencial_ligacao           = np.arange(0, 100, 1)

        # Generate fuzzy membership functions
        self.intensidade_interacoes_AC_baixa   = fuzz.trimf(self.x_intensidade_interacoes_AC, [0, 0, 30])
        self.intensidade_interacoes_AC_alta    = fuzz.trapmf(self.x_intensidade_interacoes_AC, [10, 30, 100, 100])
        self.intensidade_interacoes_BC_baixa   = fuzz.trimf(self.x_intensidade_interacoes_BC, [0, 0, 30])
        self.intensidade_interacoes_BC_alta    = fuzz.trapmf(self.x_intensidade_interacoes_BC, [10, 30, 100, 100])

        self.similaridade_entre_vertices_baixa = fuzz.trimf(self.x_similaridade_entre_vertices, [0, 0, 60])
        self.similaridade_entre_vertices_alta  = fuzz.trimf(self.x_similaridade_entre_vertices, [40, 100, 100])
        
        self.idade_interacoes_AC_baixa         = fuzz.trimf(self.x_idade_interacoes_AC, [0, 0, 2])
        self.idade_interacoes_AC_alta          = fuzz.trimf(self.x_idade_interacoes_AC, [1, 3, 3])
        self.idade_interacoes_BC_baixa         = fuzz.trimf(self.x_idade_interacoes_BC, [0, 0, 2])
        self.idade_interacoes_BC_alta          = fuzz.trimf(self.x_idade_interacoes_BC, [1, 3, 3])
        
        self.potencial_ligacao_baixo           = fuzz.trimf(self.x_potencial_ligacao, [0, 0, 60])
        self.potencial_ligacao_medio           = fuzz.trimf(self.x_potencial_ligacao, [10, 50, 90])
        self.potencial_ligacao_alto            = fuzz.trimf(self.x_potencial_ligacao, [40, 100, 100])
    
        self.grau_intensidade_interacoes_AC_baixa   = fuzz.interp_membership(self.x_intensidade_interacoes_AC, self.intensidade_interacoes_AC_baixa, intensidade_interacoes_AC)
        self.grau_intensidade_interacoes_AC_alta    = fuzz.interp_membership(self.x_intensidade_interacoes_AC, self.intensidade_interacoes_AC_alta, intensidade_interacoes_AC)

        self.grau_intensidade_interacoes_BC_baixa   = fuzz.interp_membership(self.x_intensidade_interacoes_BC, self.intensidade_interacoes_BC_baixa, intensidade_interacoes_BC)
        self.grau_intensidade_interacoes_BC_alta    = fuzz.interp_membership(self.x_intensidade_interacoes_BC, self.intensidade_interacoes_BC_alta, intensidade_interacoes_BC)

        self.grau_similaridade_entre_vertices_baixa = fuzz.interp_membership(self.x_similaridade_entre_vertices, self.similaridade_entre_vertices_baixa, similaridade_entre_vertices)
        self.grau_similaridade_entre_vertices_alta  = fuzz.interp_membership(self.x_similaridade_entre_vertices, self.similaridade_entre_vertices_alta, similaridade_entre_vertices)

        self.grau_idade_interacoes_AC_baixa         = fuzz.interp_membership(self.x_idade_interacoes_AC, self.idade_interacoes_AC_baixa, self.idade_interacoes_AC)
        self.grau_idade_interacoes_AC_alta          = fuzz.interp_membership(self.x_idade_interacoes_AC, self.idade_interacoes_AC_alta, self.idade_interacoes_AC)

        self.grau_idade_interacoes_BC_baixa         = fuzz.interp_membership(self.x_idade_interacoes_BC, self.idade_interacoes_BC_baixa, self.idade_interacoes_BC)
        self.grau_idade_interacoes_BC_alta          = fuzz.interp_membership(self.x_idade_interacoes_BC, self.idade_interacoes_BC_alta, self.idade_interacoes_BC)
        
        active_rule1 = np.fmin(self.grau_intensidade_interacoes_AC_alta, np.fmin(self.grau_intensidade_interacoes_BC_alta, np.fmin(self.grau_similaridade_entre_vertices_alta, np.fmin(self.grau_idade_interacoes_AC_baixa, self.grau_idade_interacoes_BC_baixa))))
        potencial_ligacao_rule1 = np.fmin(active_rule1, self.potencial_ligacao_alto)
        print('active_rule1 ', active_rule1)
        

        active_rule2 = np.fmin(self.grau_intensidade_interacoes_AC_baixa, np.fmin(self.grau_intensidade_interacoes_BC_baixa, np.fmin(self.grau_similaridade_entre_vertices_baixa, np.fmin(self.grau_idade_interacoes_AC_alta, self.grau_idade_interacoes_BC_alta))))
        potencial_ligacao_rule2 = np.fmin(active_rule2, self.potencial_ligacao_baixo)
        print('active_rule2 ', active_rule2)
        #print('potencial_ligacao_rule2 ', potencial_ligacao_rule2)

        active_rule3 = np.fmin(self.grau_intensidade_interacoes_AC_alta, np.fmin(self.grau_intensidade_interacoes_BC_alta, np.fmin(self.grau_similaridade_entre_vertices_baixa, np.fmin(self.grau_idade_interacoes_AC_baixa, self.grau_idade_interacoes_BC_baixa))))
        potencial_ligacao_rule3 = np.fmin(active_rule3, self.potencial_ligacao_medio)
        print('active_rule3 ', active_rule3)
        #print('potencial_ligacao_rule3 ', potencial_ligacao_rule3)

        active_rule4 = np.fmin(self.grau_intensidade_interacoes_AC_baixa, np.fmin(self.grau_intensidade_interacoes_BC_baixa, np.fmin(self.grau_similaridade_entre_vertices_alta, np.fmin(self.grau_idade_interacoes_AC_baixa, self.grau_idade_interacoes_BC_baixa))))
        potencial_ligacao_rule4 = np.fmin(active_rule4, self.potencial_ligacao_medio)
        print('active_rule4 ', active_rule4)
        #print('potencial_ligacao_rule4 ', potencial_ligacao_rule4)
        
        active_rule5 = np.fmin(self.grau_intensidade_interacoes_AC_baixa, np.fmin(self.grau_intensidade_interacoes_BC_baixa, np.fmin(self.grau_similaridade_entre_vertices_alta, np.fmin(self.grau_idade_interacoes_AC_alta, self.grau_idade_interacoes_BC_alta))))
        potencial_ligacao_rule5 = np.fmin(active_rule5, self.potencial_ligacao_baixo)
        print('active_rule5 ', active_rule5)
        
        
        # Aggregate all three output membership functions together
        aggregated = np.fmax(potencial_ligacao_rule1,
                             np.fmax(potencial_ligacao_rule2, np.fmax( np.fmax(potencial_ligacao_rule3, potencial_ligacao_rule4), potencial_ligacao_rule5)   ))

        # Calculate defuzzified result
        self.potencial_ligacao = fuzz.defuzz(self.x_potencial_ligacao, aggregated, 'centroid')
        
        self.grau_potencial_ligacao = fuzz.interp_membership(self.x_potencial_ligacao, aggregated, self.potencial_ligacao)
        
        if ShowGraphics:
            fig, ax0 = plt.subplots(figsize=(8, 3))
  
            ax0.plot(self.x_intensidade_interacoes_AC, self.intensidade_interacoes_AC_baixa, 'b', linewidth=0.5, linestyle='--', )
            ax0.plot(self.x_intensidade_interacoes_AC, self.intensidade_interacoes_AC_alta, 'r', linewidth=0.5, linestyle='--')
            ax0.set_title('Regra de Intensidade')
            
            
            # Turn off top/right axes
            for ax in (ax0,):
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.get_xaxis().tick_bottom()
                ax.get_yaxis().tick_left()
  
            plt.tight_layout()
            
            fig, ax0 = plt.subplots(figsize=(8, 3))
  
            ax0.plot(self.x_similaridade_entre_vertices, self.similaridade_entre_vertices_baixa, 'b', linewidth=0.5, linestyle='--', )
            ax0.plot(self.x_similaridade_entre_vertices, self.similaridade_entre_vertices_alta, 'r', linewidth=0.5, linestyle='--')
            ax0.set_title('Regra de Similaridade')
            
            
            # Turn off top/right axes
            for ax in (ax0,):
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.get_xaxis().tick_bottom()
                ax.get_yaxis().tick_left()
  
            plt.tight_layout()
            
  
            fig, ax0 = plt.subplots(figsize=(8, 3))
  
            ax0.plot(self.x_idade_interacoes_AC, self.idade_interacoes_AC_baixa, 'b', linewidth=0.5, linestyle='--', )
            ax0.plot(self.x_idade_interacoes_AC, self.idade_interacoes_AC_alta, 'r', linewidth=0.5, linestyle='--')
            ax0.set_title('Regra de Idade')
            
            
            # Turn off top/right axes
            for ax in (ax0,):
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.get_xaxis().tick_bottom()
                ax.get_yaxis().tick_left()
  
            plt.tight_layout()
  
  
  
            plt.show()





if __name__ == '__main__':
    intensidadeAC = 1
    intensidadeBC = 1
    Similaridade = 70.0
    IdadeAC = 0
    IdadeBC = 0
    data = FuzzyCalculation(intensidadeAC, intensidadeBC, Similaridade, IdadeAC, IdadeBC, False)
    print "Grau Potencial de Ligacao: ", data.grau_potencial_ligacao
    print "Potencial de Ligacao: ", data.potencial_ligacao
    
    