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