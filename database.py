# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:39:03 2016

@author: Kristen
"""

import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

with con:
    
    cur= con.cursor()
    cur.execute('DROP TABLE IF EXISTS <weather>;')
    cur.execute('DROP TABLE IF EXISTS <cities>;')
    cur.execute('CREATE TABLE cities(name,state);')
    cur.execute('.separator ","')
    cur.execute('.import cities.txt cities;')
	cur.execute('CREATE TABLE weather(name,state);')
    cur.execute('.separator ","')
    cur.execute('.import weather.txt weather;')
	cur.execute('SELECT name, state, warm_month) FROM cities INNER JOIN weather ON name city;')
	
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df=pd.DataFrame(rows, columns=cols)
	
	