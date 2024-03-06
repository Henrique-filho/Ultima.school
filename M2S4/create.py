import sqlite3
import datetime
conexao = sqlite3.connect('tranznx_database.db')
cursor = conexao.cursor()

sql_cliente = ''' CREATE TABLE cliente (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT,
                cnpj TEXT NOT NULL,
                CONSTRAINT cliente_UN UNIQUE (cnpj))

'''
cursor.execute(sql_cliente)


sql_nfe = ''' CREATE TABLE nfe(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                data_emissao DATE,
                metragem INTEGER,
                numero_nfe INTEGER,
                cliente_id INTEGER,
                CONSTRAINT nfe_FK FOREIGN KEY (cliente_id) REFERENCES cliente(id))
'''
cursor.execute(sql_nfe)

sql_vendas = ''' CREATE TABLE vendas (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    data_entrega DATE,
                    numero_nfe INTEGER,
                    cliente_id INTEGER,
                    metragem INTEGER,
                    venda_id INTEGER,
                    CONSTRAINT venda_FK FOREIGN KEY (numero_nfe) REFERENCES nfe(id))
'''

cursor.execute(sql_vendas)
conexao.commit()
conexao.close()