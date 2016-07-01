# coding=UTF-8
import numpy as np
import csv
import openpyxl
import urllib2
import json
import sqlite3
import re
import nltk

def distinguish(my_list,my_dictionary):
	for stuff in my_list:
		if re.search(r'\w+\s\w+',stuff):
			tokens = nltk.word_tokenize(stuff)
			query_database(tokens,my_dictionary,True)
		else:
			query_database(stuff,my_dictionary,False)


def query_database(my_stem,my_dictionary,phrases):
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	conn.text_factory = str
	if phrases == False:
		t = (my_stem.lower(),)
		rows = c.execute('SELECT * FROM common_words_chinese WHERE stem=?', t) 	
		for row in rows:
			my_dictionary[row[1]] = row[2]
	elif phrases == True:
		stem_dic = ""
		kk_dic = ""
		for stuff in my_stem:
			t = (stuff.encode('utf8'),)
			rows = c.execute('SELECT * FROM common_words_chinese WHERE stem=?', t)
			for row in rows:
				stem_dic = stem_dic + " " + str(row[1])
				kk_dic = kk_dic + " " + str(row[2]) 			
		my_dictionary[stem_dic[1:]] = kk_dic[1:]



