import requests

def header(funcao):
    def marketcap():
        print('Marketcap USD-BRL')
    return marketcap

@header
def cotacao_dolar():
    link = f"https://economia.awesomeapi.com.br/last/USD-BRL"
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

cotacao_dolar() 
 raise except