# -*- coding: utf-8 -*-
"""
Importing a sample of PNAD 2012
Funcional e OO
Data Science - IMIH
Prof. Neylson
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
#pnad.V4720.astype('float') # tem Sem declaração. Tem que transf em np.nan
pnad.V4729.describe()

# Tira a média e a média ponderada pelo peso amostral da idade
np.mean(pnad.V8005)
np.average(pnad.V8005, weights = pnad.V4729)
# Veja a diferença!

"""
Para outras estatísticas com peso amostral, utilizar a classe 
statsmodels.stats.weightstats.DescrStatsW
do pacote statsmodels
"""

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

# Arrumando a variável V4803 - escolaridade
pnad.V4803.value_counts()
pnad['esc'] = pnad.V4803
pnad.loc[pnad['V4803'] == 'Sem instrução e menos de 1 ano', 'esc'] = 0
pnad.loc[pnad['V4803'] == '1 ano', 'esc'] = 1
pnad.loc[pnad['V4803'] == '2 anos', 'esc'] = 2
pnad.loc[pnad['V4803'] == '3 anos', 'esc'] = 3
pnad.loc[pnad['V4803'] == '4 anos', 'esc'] = 4
pnad.loc[pnad['V4803'] == '5 anos', 'esc'] = 5
pnad.loc[pnad['V4803'] == '6 anos', 'esc'] = 6
pnad.loc[pnad['V4803'] == '7 anos', 'esc'] = 7
pnad.loc[pnad['V4803'] == '8 anos', 'esc'] = 8
pnad.loc[pnad['V4803'] == '9 anos', 'esc'] = 9
pnad.loc[pnad['V4803'] == '10 anos', 'esc'] = 10
pnad.loc[pnad['V4803'] == '11 anos', 'esc'] = 11
pnad.loc[pnad['V4803'] == '12 anos', 'esc'] = 12
pnad.loc[pnad['V4803'] == '13 anos', 'esc'] = 13
pnad.loc[pnad['V4803'] == '14 anos', 'esc'] = 14
pnad.loc[pnad['V4803'] == '15 anos ou mais', 'esc'] = 15
pnad.loc[pnad['V4803'] == 'Não determinados ', 'esc'] = np.nan

pnad['esc'] = pnad['esc'].astype('float')

pnad['esc'].describe().round(2)
pnad['esc'].mean()

# Calculando a média ponderada pelo peso amostral
escSemNa = pnad.loc[pnad['esc'].notna(), 'esc']
pesoEsc  = pnad.loc[pnad['esc'].notna(), 'V4729']

np.average(escSemNa, weights = pesoEsc) # Não mudou muito



# Fazendo uma tabela de frequência de uma variável
tab = pd.crosstab(index=pnad['V0404'],  # Make a crosstab
                              columns="count")      # Name the count column

print('Distribuição de Frequências' + '\n')
print(tab)

print('Distribuição de porcentagens' + '\n')
print((tab / tab.sum())*100)

# Fazendo uma tabela de freqência de duas variáveis
tab2 = pd.crosstab(index=pnad.V0404, columns = pnad.V0302, margins = True)
print(tab2)

# Tabelas de frequência com porcentagens
tab2_percent_row = pd.crosstab(index=pnad.V0404, columns = pnad.V0302, 
                           margins = True, normalize = 'index') * 100
print(tab2_percent_row)

tab2_percent_col = pd.crosstab(index=pnad.V0404, columns = pnad.V0302, 
                           margins = True, normalize = 'columns') * 100
print(tab2_percent_col)

tab2_percent_all = pd.crosstab(index=pnad.V0404, columns = pnad.V0302, 
                           margins = True, normalize = 'all') * 100
print(tab2_percent_all)


### Algumas visualizações
# Histograma
sns.set(font_scale=1)
fig, ax = plt.subplots()
fig.set_size_inches(8, 4)
sns.distplot(pnad.V4720.dropna(), kde = False)
plt.title('Distribuição de renda - PNAD 2012')
plt.xlabel('Renda')
plt.ylabel('Frequência')
plt.show()

# Densidade
fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
sns.distplot(pnad.V4720.dropna(), hist = False)
plt.title('Distribuição de renda - PNAD 2012')
plt.xlabel('Renda')
plt.ylabel('Gaussian Kernel Density Estimate')
plt.show()

# Cruzando renda e idade
sns.jointplot(x = pnad.V4720, y = pnad.V8005, size = 8)
plt.show()


fig, ax = plt.subplots()
fig.set_size_inches(8, 6)
plt.scatter(x = pnad.V4720, y = pnad.V8005)
plt.title('Gráfico de dispersão - Scatterplot', fontsize = 14)
plt.xlabel("Renda")
plt.ylabel("Idade")
plt.show()


### Plotando sexo e cor
sns.set(color_codes = True)
sns.countplot(x = pnad.V0302)
plt.show()

sns.countplot(y = pnad.V0302, color = 'c')
plt.show()


# Cruzando sexo e idade
sns.boxplot(x = pnad.V0302, y = pnad.V8005)
plt.show()

sns.boxplot(y = pnad.V0302, x = pnad.V8005)
plt.show()



