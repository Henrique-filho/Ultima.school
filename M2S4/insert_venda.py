import sqlite3
import datetime
conexao = sqlite3.connect('tranznx_database.db')
cursor = conexao.cursor()

print(' VENDAS CADASTRADAS ATÉ O MOMENTO: ')

sql1 = '''SELECT * FROM vendas '''

# Executar a consulta
cursor.execute(sql1)

# Recuperar os resultados da consulta
resultados = cursor.fetchall()

if not resultados:  
    print('NENHUMA VENDA CADASTRADA.')
else:
    for cliente in resultados:
        print(cliente)  



data_romaneio = input("Digite a data do romaneio: ")

razao_social = input(" Digite a razao social do cliente: ")

nfe = input('Digite o numero da NFe: ')

volume_romaneio = input("Digite a quantidade de metros: ")



valores1 = [ data_romaneio, razao_social, nfe, volume_romaneio]


sql2 = '''INSERT INTO vendas (data_romaneio, razao_social, nfe, volume_romaneio ) VALUES (?, ?, ?, ?)

'''


cursor.execute(sql2, valores1)

print('VENDA CADASTRADA COM SUCESSO!')

conexao.commit()
conexao.close()