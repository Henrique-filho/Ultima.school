  
texto = input('Digite sua Frase')
n_letras = len(texto)
x=-1
for i in range(n_letras):
    print(texto[i])
    if texto[i] == 'a':
        x = x+1
print(x)
    
