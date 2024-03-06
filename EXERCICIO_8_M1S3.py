texto = input('Digite a 1° Frase')
texto_2 = input('Disgita a 2° frase')
tam_texto1 = len(texto)
z = True
for i in range(tam_texto1):
    if texto[i] == texto_2[i]:
        x = True
    else:
        z = False
if x == True and z == True:
    print('há prefixo nas palavras.')
else:
    print('não há prefixo nas palavras.')