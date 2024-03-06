import sqlite3

conexao = sqlite3.connect('M2S3')

cursor = conexao.cursor()

sql = "SELECT * FROM fornecedor WHERE produto = 'carnes' "


cursor.execute(sql)

conexao.commit()
conexao.close()