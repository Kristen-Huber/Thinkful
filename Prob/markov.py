# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:56:09 2016

@author: Kristen
"""

import pandas as pd

df=pd.DataFrame({'bull':[.9,.15,.25],
                 'bear':[.075,.8,.25],
                'stagnant':[.025,.05,.5]
                 },
                 
                 index=["bull","bear","stagnant"])