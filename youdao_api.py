# coding=UTF-8
import urllib2
import json
import opencc


the_list = ['frank','truth','demon','daj']
no_result_in_this_api = []

def youdou_api(the_list,no_result_in_this_api):
	for eachWord in the_list:
		url = 'http://fanyi.youdao.com/openapi.do?keyfrom=showmeeng&key=1890848919&type=data&doctype=json&version=1.1&q='+ eachWord
		wordinfo= urllib2.urlopen(url).read()
		data = json.loads(wordinfo)
		
		try:
			phonetic = data['basic']['us-phonetic']		
			explains = data['basic']['explains']
			phonetic = "[" + phonetic + "]"
			print eachWord
			print phonetic	
			for meaning_text in explains:
				print opencc.convert(meaning_text, config='s2tw.json')
			print '---------------'
		except KeyError:
			no_result_in_this_api.append(eachWord)
			pass	

youdao_api(the_list,no_result_in_this_api)