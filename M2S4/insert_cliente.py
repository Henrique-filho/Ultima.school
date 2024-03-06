import sqlite3
import datetime
conexao = sqlite3.connect('tranznx_database.db')

    # Criar um programa que receba os dados do usuário para inserção  de um novo
    # cliente na tabela cliente:

sql = '''INSERT INTO cliente (razao_social, cnpj ) VALUES (?, ?)

    '''

print('Insira os dados do novo cliente:')

razao_social = input("Digite a razao social do novo cliente: ")
cnpj = input("Digite o cnpj ou cpf do novo cliente: ")


valores = [razao_social, cnpj ]

cursor = conexao.cursor()

cursor.execute(sql, valores)

print(" Cadastro realizado com sucesso: ")

sql2 = ''' SELECT * FROM cliente;

    '''      

try:
    cursor.execute(sql2)
  
except sqlite3.Error as e:
    print("Erro ao executar a consulta SQL:", e)

conexao.commit()
conexao.close()