
rows = c.execute('SELECT * FROM {} WHERE stem = ?'.format(table_name), (stem,))