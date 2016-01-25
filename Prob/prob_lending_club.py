# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:24:55 2016

@author: Kristen
"""

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

df= pd.read_csv('loansData.csv')

df.dropna(inplace=True)

plt.figure()

df.boxplot(column='Amount.Requested')
plt.savefig('loanDataBoxplot.png')

plt.figure()

df.hist(column='Amount.Requested', histtype="bar")
plt.savefig('loanDataHistogram.png')

plt.figure()
Graph=stats.probplot(df['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('loanDataQQplot.png')