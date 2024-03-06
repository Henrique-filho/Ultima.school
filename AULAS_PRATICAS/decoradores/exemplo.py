def primeiro_decorador(funcao):
    def segunda_funcao():
        print("Oque esta acontecendo antes da funcao")
        funcao()
        print("Oque ha de novo depois da funcao")
    return segunda_funcao
    
@primeiro_decorador
def funcao():
    print("executando sei que num sei o que la mais")

funcao()