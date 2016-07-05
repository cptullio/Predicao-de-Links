'''
Created on jun 3rd 2016

@author: Ronaldo Goldschmidt

Based on scikit-fuzzy


'''
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generate universe variables
x_intensidade_interacoes_AC   = np.arange(0, 10, 1)
x_intensidade_interacoes_BC   = np.arange(0, 10, 1)
x_similaridade_entre_vertices = np.arange(0, 101, 1)
x_idade_interacoes_AC         = np.arange(0, 10, 1)
x_idade_interacoes_BC         = np.arange(0, 10, 1)
x_potencial_ligacao           = np.arange(0, 100, 1)

# Generate fuzzy membership functions
intensidade_interacoes_AC_baixa   = fuzz.trimf(x_intensidade_interacoes_AC, [0, 0, 6])
intensidade_interacoes_AC_alta    = fuzz.trapmf(x_intensidade_interacoes_AC, [2, 6, 10, 10])
intensidade_interacoes_BC_baixa   = fuzz.trimf(x_intensidade_interacoes_BC, [0, 0, 6])
intensidade_interacoes_BC_alta    = fuzz.trapmf(x_intensidade_interacoes_BC, [2, 6, 10, 10])
similaridade_entre_vertices_baixa = fuzz.trimf(x_similaridade_entre_vertices, [0, 0, 60])
similaridade_entre_vertices_alta  = fuzz.trimf(x_similaridade_entre_vertices, [40, 100, 100])
idade_interacoes_AC_baixa         = fuzz.trimf(x_idade_interacoes_AC, [0, 0, 6])
idade_interacoes_AC_alta          = fuzz.trimf(x_idade_interacoes_AC, [4, 10, 10])
idade_interacoes_BC_baixa         = fuzz.trimf(x_idade_interacoes_BC, [0, 0, 6])
idade_interacoes_BC_alta          = fuzz.trimf(x_idade_interacoes_BC, [4, 10, 10])
potencial_ligacao_baixo           = fuzz.trimf(x_potencial_ligacao, [0, 0, 60])
potencial_ligacao_medio           = fuzz.trimf(x_potencial_ligacao, [10, 50, 90])
potencial_ligacao_alto            = fuzz.trimf(x_potencial_ligacao, [40, 100, 100])



#Caso 1 Vertices que interagem muito, sobre assuntos similares e com interacoes recentes
intensidade_interacoes_AC   = 1
intensidade_interacoes_BC   = 4
similaridade_entre_vertices = 100
idade_interacoes_AC         = 0
idade_interacoes_BC         = 0

"""1 4 100.0 0 0

#Caso 2 Vertices que interagem pouco, sobre assuntos distintos e sem interacoes recentes
intensidade_interacoes_AC   = 2
intensidade_interacoes_BC   = 3
similaridade_entre_vertices = 40 
idade_interacoes_AC         = 9
idade_interacoes_BC         = 8



#Caso 3 Vertices que interagem muito, sobre assuntos distintos e com interacoes recentes
intensidade_interacoes_AC   = 7
intensidade_interacoes_BC   = 8
similaridade_entre_vertices = 30 
idade_interacoes_AC         = 1
idade_interacoes_BC         = 2



#Caso 4 Vertices que interagem pouco, sobre assuntos similares e com interacoes recentes
intensidade_interacoes_AC   = 3
intensidade_interacoes_BC   = 2
similaridade_entre_vertices = 80 
idade_interacoes_AC         = 3
idade_interacoes_BC         = 1

"""

"""

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(x_idade, idade_jovem, 'b', linewidth=1.5, label='Jovem')
ax0.plot(x_idade, idade_meiaidade, 'r', linewidth=1.5, label='Meia Idade')
ax0.set_title('Idade')
ax0.legend()

ax1.plot(x_pressao, pressao_baixa, 'b', linewidth=1.5, label='Baixa')
ax1.plot(x_pressao, pressao_alta, 'r', linewidth=1.5, label='Alta')
ax1.set_title('Pressao')
ax1.legend()

ax2.plot(x_seguro, seguro_baixo, 'b', linewidth=1.5, label='Baixo')
ax2.plot(x_seguro, seguro_alto, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Valor Seguro')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
"""


"""
.. image:: PLOT2RST.current_figure
Fuzzy rules
-----------
Now, to make these triangles useful, we define the *fuzzy relationship*
between input and output variables. For the purposes of our example, consider
two simple rules:
1. If age is half age AND blood pressure is low, then the insurance will be low
2. If age is young AND blood pressure is high, then the insurance will be high
"""

grau_intensidade_interacoes_AC_baixa   = fuzz.interp_membership(x_intensidade_interacoes_AC, intensidade_interacoes_AC_baixa, intensidade_interacoes_AC)
grau_intensidade_interacoes_AC_alta    = fuzz.interp_membership(x_intensidade_interacoes_AC, intensidade_interacoes_AC_alta, intensidade_interacoes_AC)

grau_intensidade_interacoes_BC_baixa   = fuzz.interp_membership(x_intensidade_interacoes_BC, intensidade_interacoes_BC_baixa, intensidade_interacoes_BC)
grau_intensidade_interacoes_BC_alta    = fuzz.interp_membership(x_intensidade_interacoes_BC, intensidade_interacoes_BC_alta, intensidade_interacoes_BC)

grau_similaridade_entre_vertices_baixa = fuzz.interp_membership(x_similaridade_entre_vertices, similaridade_entre_vertices_baixa, similaridade_entre_vertices)
grau_similaridade_entre_vertices_alta  = fuzz.interp_membership(x_similaridade_entre_vertices, similaridade_entre_vertices_alta, similaridade_entre_vertices)

grau_idade_interacoes_AC_baixa         = fuzz.interp_membership(x_idade_interacoes_AC, idade_interacoes_AC_baixa, idade_interacoes_AC)
grau_idade_interacoes_AC_alta          = fuzz.interp_membership(x_idade_interacoes_AC, idade_interacoes_AC_alta, idade_interacoes_AC)

grau_idade_interacoes_BC_baixa         = fuzz.interp_membership(x_idade_interacoes_BC, idade_interacoes_BC_baixa, idade_interacoes_BC)
grau_idade_interacoes_BC_alta          = fuzz.interp_membership(x_idade_interacoes_BC, idade_interacoes_BC_alta, idade_interacoes_BC)


print('intensidade_interacoes_AC ', intensidade_interacoes_AC)
print('grau_intensidade_interacoes_AC_baixa ', grau_intensidade_interacoes_AC_baixa)
print('grau_intensidade_interacoes_AC_alta ', grau_intensidade_interacoes_AC_alta)

print('intensidade_interacoes_BC ', intensidade_interacoes_BC)
print('grau_intensidade_interacoes_BC_baixa ', grau_intensidade_interacoes_BC_baixa)
print('grau_intensidade_interacoes_BC_alta ', grau_intensidade_interacoes_BC_alta)

print('similaridade_entre_vertices ', similaridade_entre_vertices)
print('grau_similaridade_entre_vertices_baixa ', grau_similaridade_entre_vertices_baixa)
print('grau_similaridade_entre_vertices_alta ', grau_similaridade_entre_vertices_alta)

print('idade_interacoes_AC ', idade_interacoes_AC)
print('grau_idade_interacoes_AC_baixa ', grau_idade_interacoes_AC_baixa)
print('grau_idade_interacoes_AC_alta ', grau_idade_interacoes_AC_alta)

print('idade_interacoes_BC ', idade_interacoes_BC)
print('grau_idade_interacoes_BC_baixa ', grau_idade_interacoes_BC_baixa)
print('grau_idade_interacoes_BC_alta ', grau_idade_interacoes_BC_alta)



active_rule1 = np.fmin(grau_intensidade_interacoes_AC_alta, np.fmin(grau_intensidade_interacoes_BC_alta, np.fmin(grau_similaridade_entre_vertices_alta, np.fmin(grau_idade_interacoes_AC_baixa, grau_idade_interacoes_BC_baixa))))
potencial_ligacao_rule1 = np.fmin(active_rule1, potencial_ligacao_alto)
print('active_rule1 ', active_rule1)
#print('potencial_ligacao_rule1 ', potencial_ligacao_rule1)

active_rule2 = np.fmin(grau_intensidade_interacoes_AC_baixa, np.fmin(grau_intensidade_interacoes_BC_baixa, np.fmin(grau_similaridade_entre_vertices_baixa, np.fmin(grau_idade_interacoes_AC_alta, grau_idade_interacoes_BC_alta))))
potencial_ligacao_rule2 = np.fmin(active_rule2, potencial_ligacao_baixo)
print('active_rule2 ', active_rule2)
#print('potencial_ligacao_rule2 ', potencial_ligacao_rule2)

active_rule3 = np.fmin(grau_intensidade_interacoes_AC_alta, np.fmin(grau_intensidade_interacoes_BC_alta, np.fmin(grau_similaridade_entre_vertices_baixa, np.fmin(grau_idade_interacoes_AC_baixa, grau_idade_interacoes_BC_baixa))))
potencial_ligacao_rule3 = np.fmin(active_rule3, potencial_ligacao_medio)
print('active_rule3 ', active_rule3)
#print('potencial_ligacao_rule3 ', potencial_ligacao_rule3)

active_rule4 = np.fmin(grau_intensidade_interacoes_AC_baixa, np.fmin(grau_intensidade_interacoes_BC_baixa, np.fmin(grau_similaridade_entre_vertices_alta, np.fmin(grau_idade_interacoes_AC_baixa, grau_idade_interacoes_BC_baixa))))
potencial_ligacao_rule4 = np.fmin(active_rule4, potencial_ligacao_medio)
print('active_rule4 ', active_rule4)
#print('potencial_ligacao_rule4 ', potencial_ligacao_rule4)

"""

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(x_seguro, seguro0, seguro_activation_baixo, facecolor='b', alpha=0.7)
ax0.plot(x_seguro, seguro_baixo, 'b', linewidth=0.5, linestyle='--', )
ax0.fill_between(x_seguro, seguro0, seguro_activation_alto, facecolor='g', alpha=0.7)
ax0.plot(x_seguro, seguro_alto, 'r', linewidth=0.5, linestyle='--')
ax0.set_title('Output membership activity')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
"""

"""
.. image:: PLOT2RST.current_figure
Rule aggregation
----------------
With the *activity* of each output membership function known, all output
membership functions must be combined. This is typically done using a
maximum operator. This step is also known as *aggregation*.
Defuzzification
---------------
Finally, to get a real world answer, we return to *crisp* logic from the
world of fuzzy membership functions. For the purposes of this example
the centroid method will be used.
---------------------------------
"""

# Aggregate all three output membership functions together
aggregated = np.fmax(potencial_ligacao_rule1,
                     np.fmax(potencial_ligacao_rule2, np.fmax(potencial_ligacao_rule3, potencial_ligacao_rule4)))

# Calculate defuzzified result
potencial_ligacao = fuzz.defuzz(x_potencial_ligacao, aggregated, 'centroid')
print(potencial_ligacao)
grau_potencial_ligacao = fuzz.interp_membership(x_potencial_ligacao, aggregated, potencial_ligacao)  # for plot
print grau_potencial_ligacao

