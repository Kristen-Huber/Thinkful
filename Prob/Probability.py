# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:00:09 2016

@author: Kristen
"""


import collections
import matplotlib.pyplot as plt
import scipy.stats as stats

data=[]

response=""

item=""


def add_to_list(item, data):
    item=raw_input("Please enter your data one-by-one. Enter Q to quit:")
    if item == "Q":
        print str(data)        
        user_input(response)
    elif item is not "Q":
        data.append(float(item))
        add_to_list(item, data)


def find_frequency(items):
    c = collections.Counter(data)
    count_sum = sum(c.values())
    for k,v in c.items():
        print("The frequency of number " + str(k) + " is " + str(float(v)/count_sum) + "\n")
    
def show_boxplot(items):
    plt.figure()
    plt.boxplot(data)
    plt.show()
    
def show_histogram(items):
    plt.figure()
    plt.hist(data,histtype='bar')
    plt.show()
    
def show_QQplot(items):
    plt.figure()    
    stats.probplot(data, dist="norm", plot= plt)
    plt.show()
    
def user_input(response):
    while response is not "quit":
        print("\n"+"What would you like to see of this data set?" )
        print("Type 'quit' at any time to quit")
        print("'F' for frequency, 'B' for boxplot, 'H' for histogram, and 'Q' for a QQ plot")
        response=raw_input("")
        if response == "F":
            find_frequency(data)
        elif response == "H":
            show_histogram(data)
        elif response == "B":
            show_boxplot(data)
        elif response == "Q":
            show_QQplot(data)
        elif response == "quit":
            break
        else:
            print("Please enter a valid character" + "\n")
            user_input(response)
        
add_to_list(item, data)


        
