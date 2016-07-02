# coding=UTF-8
import numpy as np
import csv
import openpyxl
import urllib2
import json
import sqlite3
import re
import nltk

def get_kk(my_stem,my_dictionary,phrases,table_name,cursor):
	if phrases == False: 
		t = (my_stem.lower(),)
		try:		
			rows = cursor.execute('SELECT * FROM {} WHERE stem=?'.format(table_name), t)
			for row in rows:
				my_dictionary[my_stem] = row[2]
		
		except KeyError:
			my_dictionary[my_stem] = "" 	
		
		return my_dictionary
	
	elif phrases == True:
		kk_dic = ""
		stem_string = ""
		for token in my_stem:
			t = (token,)
			try:
				rows = cursor.execute('SELECT * FROM {} WHERE stem=?'.format(table_name), t)
				for row in rows:
					kk_dic = kk_dic + " " + str(row[2])
			except KeyError:
				pass 			
			stem_string = stem_string + ' ' + str(token)
		my_dictionary[stem_string[1:]] = kk_dic[1:]	
		return my_dictionary


