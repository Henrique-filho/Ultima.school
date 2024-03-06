def primeiro_decorator(func):

    def primeira_func():
        print("Execução antes")

        func()

        print("Execução depois")

    return primeira_func

@primeiro_decorator
def funcao_utilizadora():
    print("Utilizar o decorator")

funcao_utilizadora()