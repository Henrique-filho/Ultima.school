def paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "Impar"

while True:
    print('1-par impar, 2- sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1 :
        numero = int(input('digite um numero: '))
        resultado = paridade(numero)
        print(f'O numero digitado : {numero} é {resultado}.')
    elif opcao == 2:
        print("programa finalizado")
        break
    