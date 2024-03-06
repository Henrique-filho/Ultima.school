import requests

# Nome da moeda que desejamos obter informações
coin = "bitcoin"

# URL da API CoinGecko
url = f"https://api.coingecko.com/api/v3/coins/{coin}"

# Fazendo a solicitação para a API
response = requests.get(url)
# Verificando se a solicitação foi bem sucedida
if response.status_code == 200:
    # Convertendo a resposta da API para um dicionário
    data = response.json()
else:
    print("Ocorreu um erro ao obter os dados da API.")
data
# Verificando as Keys do nosso Dict afim de localizar a de nosso interesse
data.keys()
# Verificando as Keys do nosso Dict afim de localizar a de nosso interesse
data["market_data"].keys()
# Printando o valor do BTC
data["market_data"]["current_price"]

class BitcoinIterator:
    """
    Classe que itera sobre os preços atuais de uma moeda obtidos de uma API.
    
    Atributos:
        preços (dict): Dicionário com informações sobre os preços atuais da moeda em diferentes moedas.
        current (int): Índice atual do dicionário de preços.
        end (int): Tamanho do dicionário de preços.
    
    Métodos:
        __iter__: Implementação padrão do método mágico __iter__.
        __next__: Implementação padrão do método mágico __next__.
    """
    def __init__(self, coin_name: str):
        """
        Construtor da classe.
        
        Argumentos:
            coin_name (str): Nome da moeda a ser buscada na API.
        """
        
        # Nome da moeda que desejamos obter informações
        coin = coin_name

        # URL da API CoinGecko
        url = f"https://api.coingecko.com/api/v3/coins/{coin}"

        # Fazendo a solicitação para a API
        response = requests.get(url)

        # Convertendo a resposta da API para um dicionário
        data = response.json()
        
        # Obtendo o dicionário de preços
        self.precos = data["market_data"]["current_price"]
        
        # Instanciando nosso estado atual e final
        self.current = 0
        self.end = len(self.precos)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = list(self.precos.items())[self.current]
        self.current += 1
        return result
    # Instanciando a classe com o nome da moeda que desejamos obter informações
bit = BitcoinIterator("bitcoin")

# Iterando sobre os preços em diferentes moedas
for key, value in bit.precos.items():
    print(f"O preço atual do Bitcoin em {key.upper()} é de {value:.2f}")