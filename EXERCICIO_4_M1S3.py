total = 0
while True :
    x = int(input('Digite o numero'))
    print('Total',total + x)
    total = total + x
    if x == -1 :
        print('Programa Finalizado')
        break