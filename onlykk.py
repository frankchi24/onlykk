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
from onlykk_functions import query_database,distinguish

#goals:from a column of csv getting kk,meaning

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
# if it's a word,stem it and return get the kk and meaning
# if it's a phrase, tokenize them, stem them and return kk

distinguish(words_phrases,dics)
	
#getting the kk and meaning from api


#create a excel file
wb = openpyxl.Workbook()
wb.get_sheet_names()
sheet = wb.active
sheet.title = "Cool_Stuff"
sheet = wb.get_sheet_by_name('Cool_Stuff')
x = 1

no_result = []
for stem in words_phrases:
	try:
		sheet['A%d'%x] = stem
		sheet['B%d'%x] = dics['%s'%(stem.lower())]
		conn = sqlite3.connect('test.db')
		c = conn.cursor()
		t = (stem.lower(),)
		rows = c.execute('SELECT * FROM common_words_chinese WHERE stem=?', t)  
		for row in rows:
			sheet['C%d'%x] = row[3]
			sheet['D%d'%x] = row[4]
			sheet['E%d'%x] = row[5]
			sheet['F%d'%x] = row[6]
		x = x + 1
	except KeyError:
		sheet['A%d'%x] = stem
		no_result.append(stem)
		x = x + 1	

wb.save('example.xlsx')



# create a csv file
# export the words,stem,kk and meaning to csv or excel file
# export those which can't get results from 
# filter those with multiple meanings and let user decide with meaning they want





		
# for eachWord in words:
# 	y = 0
# 	url = 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+ eachWord
# 	wordinfo= urllib2.urlopen(url).read().decode('utf-8')
# 	data = json.loads(wordinfo)
# 	try:
# 		phonetic = data['basic']['us-phonetic']		
# 		explains = data['basic']['explains']
# 	except KeyError:
# 		phonetic = ""
# 		explains = data['translation']
# 	results = "["+str(phonetic.encode('utf8'))+"]"
# 	for meaning_text in explains:
# 		results = results + ","+ meaning_text.encode('utf8')
# 		y = y + 1
# 	saveLine = eachWord + ',' + results 
# 	z = 5-y
# 	saveLine = saveLine + "," + z*"," + "\n"
# 	saveFile = open('onlykk.csv','a')
# 	saveFile.write(saveLine)
# 	saveFile.close()



