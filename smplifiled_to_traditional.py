import sqlite3
import opencc

conn = sqlite3.connect('test.db')
conn.text_factory = str
conn.row_factory = sqlite3.Row
c = conn.cursor()
table = 'test'

data_id = 1
while data_id < 18598:
	arg1 = (data_id,)
	c.execute('SELECT * FROM {} WHERE id = ?'.format(table),arg1)
	r = c.fetchone()

	x = 1
	while x < 16:
		keys = r.keys()
		if r[x] == "" or r[x] =='[]':
			x = x + 1
		else:
			holder = opencc.convert(r[x], config='s2tw.json')
			print holder 
			arg2 = (holder,data_id)
			c.execute('UPDATE {} SET {} = ? WHERE id= ?'.format(table,keys[x]),arg2)
			x = x + 1
	data_id = data_id + 1
		

conn.commit()
c.close()
conn.close()
