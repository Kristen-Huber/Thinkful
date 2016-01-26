# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:01:55 2016

@author: Kristen
"""
from scipy import stats
import collections
import pandas as pd


data= pd.read_csv('data.csv')
data.dropna(inplace=True)

freq= collections.Counter(data)
chi, p= stats.chisquare(freq.values())
if p > .05:
    print("The null hypothosis is correct.")
    
else:
    print("The null hypothesis is disproved")