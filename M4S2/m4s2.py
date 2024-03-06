''' Uma pessoa do seu time de desenvolvimento está escrevendo 
várias funções que calculam diferentes formas de gerar juros. Veja abaixo o exemplo de uma das funções:
'''

#  @decorador_imprimir
#  def juros_simples(capital, taxa, tempo):
#     return capital * (taxa / 100) * tempo'''

''' Ela pediu para você escrever um decorator chamado decorator_imprimir, que será usado para a função 
chamada imprima os parâmetros: capital, taxa e tempo, além do resultado da função.
'''

# RESOLUÇÃO DO EXERCICIO.

def decorador_imprimir(funcao):
    def juros_simples(capital, taxa, tempo):
        resultado = funcao(capital, taxa, tempo)
        print(f"capital : {capital} ")
        print(f"taxa : {taxa}")
        print(f"tempo : {tempo}")
        print(f"resultado : {resultado}\n")
        return resultado

    return juros_simples


@decorador_imprimir
def calculo_juros_simples(capital, taxa, tempo):
 #   capital = float(input("Digite o montante : "))
#   taxa = float(input("Digite a taxa de juros: "))
 #   tempo = float(input("Digite o tempo: "))
    return capital * (taxa / 100) * tempo
calculo_juros_simples(1000, 5, 6)


