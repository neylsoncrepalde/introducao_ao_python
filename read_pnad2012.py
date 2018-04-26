# -*- coding: utf-8 -*-
"""
Importing a sample of PNAD 2012
Funcional e OO
Data Science - IMIH
Prof. Neylson
"""

import pandas as pd
import numpy as np

pnad = pd.read_csv('https://github.com/neylsoncrepalde/introducao_ao_python/blob/master/pes_2012.csv?raw=true')
pnad.head()  # Verifica os primeiros casos
pnad.columns # Verifica os nomes das variáveis
pnad.dtypes  # Verifica o type de cada variável

# Tem coisa errada. Vamos consertar algumas.
pnad.UF.value_counts()
pnad.V0302.value_counts()
pnad.V0404.value_counts() # Tem 'sem declaração mas tá ok...
pnad.V8005.describe()
pnad.V4803.value_counts() # Tem que transformar em numérica
pnad.V4720.astype('float') # tem Sem declaração. Tem que transf em np.nan
pnad.V4729.describe()

# Tira a média e a média ponderada pelo peso amostral da idade
np.mean(pnad.V8005)
np.average(pnad.V8005, weights = pnad.V4729)
# Veja a diferença!

# Transformando as rendas em float
pnad.loc[pnad['V4718'] == 'Sem declaração', 'V4718'] = np.NaN
pnad.V4718 = pnad.V4718.astype('float')
pnad.loc[pnad['V4720'] == 'Sem declaração', 'V4720'] = np.NaN
pnad.V4720 = pnad.V4720.astype('float')
# Verifica
pnad[['V4718', 'V4720']].dtypes    # OK!

# Transforma as categóricas em categóricas
pnad.UF = pnad["UF"].astype('category')
pnad.V0302 = pnad.V0302.astype('category')
pnad.V0404 = pnad.V0404.astype('category')
pnad.dtypes


# Fazendo uma tabela de frequência de uma variável
tab = pd.crosstab(index=pnad['V0404'],  # Make a crosstab
                              columns="count")      # Name the count column

print('Distribuição de Frequências' + '\n')
print(tab)

print('Distribuição de porcentagens' + '\n')
print((tab / tab.sum())*100)

# Fazendo uma tabela de freqência de duas variáveis
tab2 = pd.crosstab(index=pnad.V0404, columns = pnad.V0302)
print(tab2)
