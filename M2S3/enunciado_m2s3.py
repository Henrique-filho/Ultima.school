
'''Dada a tabela “Fornecedor”, realize as operações a seguir:

(enunciado_m2s3.py)
Utilizando o comando INSERT, insira mais dois novos fornecedores:“Padaria do Pão” e
 “Marcenaria Martelo”, com os ids 3 e 4 respectivamente, e crie também os endereços;  

(update_fornecedor.py)
Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;

(select1.py)
Selecione todos os registros da tabela fornecedor com o comando SELECT;

(select2.py)
Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;

(delete.py)
Remova o fornecedor que tem o id = 1 com o comando DELETE.'''

import sqlite3

conexao = sqlite3.connect('M2S3')

cursor = conexao.cursor()

nome = input('Digite o nome do fornecedor: ')
endereco = input('Digite o endereço do fornecedor: ')
produto = input('Digite a descricao do produto: ')

sql = 'INSERT INTO fornecedor (nome, endereco, produto) VALUES (?, ?, ?)'

valores = [nome, endereco, produto]

cursor.execute(sql, valores)

conexao.commit()
conexao.close()