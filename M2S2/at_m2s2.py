''' (01)- Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. 
As tabelas devem compreender as seguintes funcionalidades:

01 - As tarefas devem ser divididas em “categorias”;
02 - Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
03 - As restrições/relacionamentos devem fazer sentido.

    (02) - Crie um programa em Python que gere tabelas para uma aplicação de eventos. 
Elas devem compreender as seguintes funcionalidades:

01 - Eventos devem ter título, data e local, além da referência ao organizador;
02 - O organizador deve ter nome, email e cpf;
03 - As restrições/relacionamentos devem fazer sentido.'''


# EXERCICIO 1
import sqlite3
conexao = sqlite3.connect('m2s2')
cursor = conexao.cursor()
cursor.execute ('''CREATE TABLE tarefas (
                id INTEGER PRIMARY KEY,
                tarefa TEXT(50),
                data VARCHAR(10),
                categoria TEXT(50),
                status TEXT(50))''')
cursor.execute('''INSERT INTO tarefas VALUES(1, 'folga', '12-11-2021', 'ar livre', 'concluido')
               ''')
conexao.commit()
conexao.close()

# EXERCICIO 2
import sqlite3
conexao = sqlite3.connect("M2s2")
cursor = conexao.cursor()
cursor.execute('''
CREATE TABLE eventos (
id INTEGER PRIMARY KEY,
evento TEXT(50),
data VARCHAR(10),
local TEXT(50),
organizador TEXT(50)               
)''')
conexao.commit()
conexao.close()

