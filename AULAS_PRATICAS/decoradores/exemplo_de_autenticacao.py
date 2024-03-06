def autenticate_decorator(funcao):
    autenticacao = '123456'
    def wrapper (*args, **kwargs):
        user_senha = input("Digite a senha: ")
        if user_senha == autenticacao:
            print("senha correta. Executando...")
            resultado = funcao(*args, **kwargs)
        else:
            print("Senha incorreta. Entrada bloqueada")
            resultado = None
        return resultado
    return wrapper

@autenticate_decorator
def realizar_transferencia():
    valor = input("Qual o valor da transferencia: ")
    data = input("Qual a data da transferencia: ")
    print(f"sua transferencia no valor de {valor}, foi agendada para a data {data}. Obrigado.")
    
    
    print("transferencia realizada")

realizar_transferencia()