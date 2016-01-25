# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:00:09 2016

@author: Kristen
"""


import collections
import matplotlib.pyplot as plt

count=0
data=[1,2,3,4,2,6,4,2,1,5,4,3,2,5,2,2]

c = collections.Counter(data)

print(c)

def find_frequency(items):
    count_sum = sum(c.values())
    
    for k,v in c.items():
        print("The frequency of number " + str(k) + " is " + str(float(v)/count_sum))
    
def save_boxplot(items):
    plt.boxplot(data)
    plt.savefig('boxplot.png')
    
def save_histogram(items):
    plt.hist(data,histtype='bar')
    plt.savefig('histogram.png')
    
find_frequency(data)
save_boxplot(data)
save_histogram(data)

        
