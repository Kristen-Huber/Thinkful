# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:13:41 2016

@author: Kristen
"""

import numpy as np
import pandas as pd
import statsmodels.api as sm



loansData=pd.read_csv('loansData.csv')

loansData['Interest.Rate']=[float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
loansData['Loan.Length']=[int(length[0:-7])for length in loansData['Loan.Length']]
loansData['FICO.Score']=[int(val.split('-')[0]) for val in loansData['FICO.Range']]

intrate=loansData['Interest.Rate']
loanamt=loansData['Amount.Requested']
fico=loansData['FICO.Score']

y=np.matrix(intrate).transpose()
x1=np.matrix(fico).transpose()
x2=np.matrix(loanamt).transpose()

x=np.column_stack([x1,x2])

X=sm.add_constant(x)
model=sm.OLS(y,X)

f=model.fit()

print(f.summary())

loansData.to_csv('loansData_clean.csv',header=True, index=False)
