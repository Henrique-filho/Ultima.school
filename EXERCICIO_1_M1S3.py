def paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"


numero = int(input())
resultado = paridade(numero)
print(resultado)


