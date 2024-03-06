import sqlite3

conexao = sqlite3.connect('M2S3')

cursor = conexao.cursor()

sql = "SELECT * FROM fornecedor"


cursor.execute(sql)

conexao.commit()
conexao.close()