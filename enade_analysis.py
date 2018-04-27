#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Estudando o Enade
Funcional e OO
@author: neylson
"""

import pandas as pd
import numpy as np

enade = pd.read_csv('https://github.com/neylsoncrepalde/introducao_ao_r/blob/master/dados/enade_2014_amostra.csv?raw=true', 
                    sep = ";")

enade.shape
enade.dtypes

enade.nu_idade.describe().round(3)
enade.nt_ger.describe().round(3)
enade.loc[enade['nt_ger'].isna(), 'nt_ger'].shape

enade.iloc[:10, :10]

enade.tp_sexo.value_counts()
enade.loc[enade['tp_sexo'] == 'N', 'tp_sexo'] = np.nan
enade['tp_sexo'] = enade['tp_sexo'].astype('category')
enade['tp_sexo'].dtype