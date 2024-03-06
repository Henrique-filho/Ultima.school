'''
import time

def decorador_time(contador):
    def temporizador():
        print("START")
        print(time.time())
        contador()
        print("END")
        print(time.time())
        return temporizador

@decorador_time
def contagem():
    for x in range (100000):
        x
    print("Oh yeah rock'n roll")

'''

import time

def decorador_time(contador):
    def temporizador():
        print("START")
        inicio = time.time()
        contador()
        fim = time.time()
        print("END")
        print(f"Tempo decorrido: {fim - inicio} segundos")
    return temporizador

@decorador_time
def contagem():
    for x in range(100000):
        pass
    print("Oh yeah rock'n roll")

contagem()