# -*- coding: utf-8 -*-
"""
Importing a sample of PNAD 2012
Funcional e OO
Data Science - IMIH
Prof. Neylson
"""

import pandas as pd

pnad = pd.read_csv('https://github.com/neylsoncrepalde/introducao_ao_python/blob/master/pes_2012.csv?raw=true')
pnad.head()

pnad.describe()
pnad.head()
pnad['V0404'].value_counts()


tab = pd.crosstab(index=pnad['V0404'],  # Make a crosstab
                              columns="count")      # Name the count column

print('Distribuição de Frequências' + '\n')
print(tab)

print('Distribuição de porcentagens' + '\n')
print((tab / tab.sum())*100)