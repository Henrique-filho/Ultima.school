import sqlite3

conexao = sqlite3.connect('M2S3')

cursor = conexao.cursor()

sql = "UPDATE fornecedor SET endereco = 'rua dos peixes 26' WHERE id = 2"


cursor.execute(sql)

conexao.commit()
conexao.close()