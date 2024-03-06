import sqlite3

conexao = sqlite3.connect('M2S3')

cursor = conexao.cursor()

sql = '''INSERT INTO fornecedor (nome, endereco, produto) 
VALUES ('padaria do pão' , 'rua dos paes 45', 'pao-frances'),
        ('marcenaria martelo', 'rua dos paes 56', 'cadeira')'''


cursor.execute(sql)

conexao.commit()
conexao.close()