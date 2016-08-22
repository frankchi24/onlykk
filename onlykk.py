# coding=UTF-8
import numpy as np
import csv
import openpyxl
import urllib2
import json
import sqlite3
import re
import nltk
import opencc
from onlykk_functions import get_kk
from youdao_api import youdao_api

#goals:from a column of csv getting kk,meaning



#get kk from the database


#import from excel file,getting a list of string
#import from csv,getting a list of string
words_phrases = np.loadtxt('stems.csv',
							delimiter = ',',
							unpack = True,
							#to specify different variables
							dtype = 'str')
words_phrases = list(words_phrases) #not sure whethter use nummpy array or not, making it a list for now
#store stems and kk and meaning in a dictionary
dics = {}
dics.setdefault('stem', 'kk')

# #distingusih between words and phrases
# stem words and return get the kk and meaning
# tokenize phrases, stem them and return kk
database_name = 'test.db'
table_name = 'common_words_chinese'


conn = sqlite3.connect(database_name)
conn.text_factory = str #beore cursor or after cursor
c = conn.cursor()

phrases = True
for stuff in words_phrases:
	if re.search(r'\w+\s\w+',stuff):
		stuff = nltk.word_tokenize(stuff)
		get_kk(stuff,dics,True,table_name,c)
	elif re.search(r'\w+\s\w+',stuff) == None:
		get_kk(stuff,dics,False,table_name,c)

# print dics['next']
# print dics['watch TV']
# print dics['scotter']

#if no results,get the kk and meaning from api, save the new stuff to the database

#create a excel file
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.active
sheet.title = "Cool_Stuff"
sheet = wb.get_sheet_by_name('Cool_Stuff')


no_kk = []
no_meaning = []
results = []

for stuff in words_phrases:
	results.append(stuff)
	try:
		results.append(dics[stuff])
	except KeyError:
		no_kk.append(stuff)
	try:
		stuff = stuff.lower()
		rows = c.execute('SELECT * FROM {} WHERE stem = ?'.format(table_name), (stuff,))
	except KeyError:
		no_meaning.append(stuff)
	for row in rows:
		for last in row[3:]:
			if last != '' and last!= None:
				print last
				results.append(last)

	
	sheet.append(results)
	results = []

# wb.save('example1.xlsx')

for no in no_kk:
	print no

print "--------"


for no in no_meaning:
	print no

# create a csv file
# export those which can't get results from 

# filter those with multiple meanings and let user decide with meaning they want




