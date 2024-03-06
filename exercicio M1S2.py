print('  ')
# ATIVIDADE 1- Calcular valor do projeto de um free lancer
print('atividade 1 - calcular valor de projeto free lancer')
print(' ')
valor_inicial = 1000
horas_estimadas = 80
valor_hora = 20.45
taxa = 0.15 
print(' ')
valor_total = (valor_inicial + horas_estimadas * valor_hora) * (1 + taxa)
print(f'{valor_total:2f}')
print('  ')
# ATIVIDADE 2 - Programa de interpolação da string de boas vindas
print("atividade 2 - sobre interpolação de strings")
print("  ")
nomes = ('Elisson', 'Giulia', 'Willian', 'Gileno')
nome_pessoa = input('Digite seu nome: ')

if nome_pessoa in nomes:
    mensagem_de_boas_vindas = f'Olá, {nome_pessoa}! Seja bem vindo à nave Imperial dos Siths.'
    print(mensagem_de_boas_vindas)
else:
    print('Desculpe, seu nome não consta na lista de nomes válidos.')

    