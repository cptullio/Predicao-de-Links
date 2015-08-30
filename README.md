# Predicao-de-Links
Projeto para Documentação e uso das técnicas de Predição de Links
Para executar a aplicação
==============
Requisitos:
==============


Python 2.7
==============

Networkx
==============

Numpy
==============

feedparser - Para baixar o arxiv
==============

psycopg2 - Para executar a base do Duarte.
==============
executando no codeanywhere:
==============

1 - Crio um servidor apontando para https://github.com/cptullio/Predicao-de-Links.git
==============
2 - executo o comando: export PYTHONPATH="$PYTHONPATH://home/cabox/workspace/PredLig/src/" 
==============
3 - sudo pip install networkx
==============
4 - sudo pip install numpy
==============
5 - sudo pip install feedparser

==============
6 - python execution/astroph/Step01.py  - para gerar o grafo
==============

7 - python execution/astroph/Step02.py  - para gerar o grafo o período de treino e teste
==============

8 - python execution/astroph/Step03.py  - para selecionar os nos não ligados no treino
==============

9 - python execution/astroph/Step04.py  - para executar os calculos
==============

10 - python execution/astroph/Step05.py  - para analisar os nós não ligados no treino verificando se eles conectados no grafo de teste
==============

11 - python execution/astroph/Step06.py  - para ordenar os calculos
==============

12 - python execution/astroph/Step07.py  - para analisar os nós ordenados com o treino
==============

13 - python execution/astroph/Step08.py  - para gerar dados estatísticos das análises
==============






