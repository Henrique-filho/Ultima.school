import sqlite3
conexao = sqlite3.connect('tranznx_database.db')
cursor = conexao.cursor() 

sql = ''' DELETE FROM vendas

'''

cursor.execute(sql)
conexao.commit()
conexao.close()