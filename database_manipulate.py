# coding=UTF-8
import sqlite3
import opencc
import re

def create_table_sorted(name):
    c.execute('''CREATE TABLE {}(  
            stem                    text, 
            kk                      text,
            abbreviation            text, 
            adjetive                text, 
            adverb                  text,
            conjunction             text,
            initial                 text,
            noun                    text,
            verb                    text,
            verb_intransitive       text,
            verb_transitive         text,
            pronoun                 text,
            preposition             text,
            num                     text,
            other                   text
            )'''.format(name))


def order_change(id_row,c):
    #get meainig and rows from a database table and make it a dictionary
    x = id_row
    arg = (x,)
    rows = c.execute('SELECT * FROM common_words_chinese WHERE id = ?', arg)
    dic = {
        'abbr.' : '',
        'adj.'  : '',
        'adv.'  : '',
        'conj.' : '',
        'int.'  : '',
        'n.'    : '',
        'v.'    : '',
        'vi.'   : '',
        'vt.'   : '',
        'v.'    : '',
        'pro.'  : '',
        'prep'  : '',
        'num.'  : '',
        'none'  : ''
    }

    column_number = 3
    for row in rows:
        stem = row[1]
        kk = row[2]
        while column_number < 9:
            y = 0
            for key in dic:
                if re.match(key,row[column_number]):
                    dic[key] = dic[key] + str(row[column_number])
                    y = y + 1
            if y == 0 and row[column_number] != '' and row[column_number] != None:
                dic['none'] = dic['none'] + str(row[column_number])
            column_number = column_number + 1

    
    #make sure there is a table called test table, if not, create one        
    c.execute('''
        INSERT INTO test(
        stem, 
        kk, 
        abbreviation, 
        adjetive,
        adverb,
        conjunction,
        initial,
        noun,
        verb,
        verb_intransitive,
        verb_transitive,
        pronoun,
        preposition,
        num,
        other
        ) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(
                    stem,
                    kk,
                    dic['abbr.'],
                    dic['adj.'] ,
                    dic['adv.'] ,
                    dic['conj.'],
                    dic['int.'] ,
                    dic['n.']   ,
                    dic['v.']   ,
                    dic['vi.']  ,
                    dic['vt.']  ,
                    dic['pro.'] ,
                    dic['prep'] ,
                    dic['num.'] ,
                    dic['none' ]
                    ))


conn = sqlite3.connect('test.db')
conn.text_factory = str
c = conn.cursor()
# create_table_sorted('test')
id_row = 1
while id_row < 18598:
    order_change(id_row,c)
    id_row = id_row + 1
conn.commit()
c.close()
conn.close()













