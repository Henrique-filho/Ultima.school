#!C:\Users\HenriqueFilho\Desktop\M4S1\.venv\Scripts\... 
import requests

class TabelaFipe:
    def __init__(self):
        self.headers = {'user-agent': 'Consulta-fipe'}
        self.marcas = None
        self.modelos = None
        self.anos = None

    def _get_marcas(self):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas'
        resposta = requests.get(url, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json()
        return []

    def _get_modelos(self, marca_id):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos'
        resposta = requests.get(url, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json().get('modelos', [])
        return []

    def _get_anos(self, marca_id, modelo_id):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos/{modelo_id}/anos/'
        resposta = requests.get(url, headers=self.headers)
        if resposta.status_code == 200:
            return resposta.json()
        return []

    def obter_todas_marcas(self):
        self.marcas = self._get_marcas()
        return self.marcas

    def obter_todos_modelos(self, marca_id):
        self.modelos = self._get_modelos(marca_id)
        return self.modelos
    
    def obter_todos_anos(self, marca_id, modelo_id):
        self.anos = self._get_anos(marca_id, modelo_id)
        return self.anos

    def obter_modelos_por_marca(self, marca_id):
        return self._get_modelos(marca_id) 
    
    def obter_informacoes_veiculo(self, marca_id, modelo_id, ano_id):
        url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos/{modelo_id}/anos/{ano_id}'
        resposta = requests.get(url, headers = self.headers)
        if resposta.status_code == 200:
            dados_veiculo = resposta.json()
            print("Dados do Veículo:")
            print(f'Modelo: {dados_veiculo["Modelo"]}')
            print(f"Marca: {dados_veiculo['Marca']}")
            print(f'Ano: {dados_veiculo["AnoModelo"]}')
            print(f"Valor: {dados_veiculo['Valor']}")
            print(f"Tipo: {dados_veiculo['Combustivel']}")
            print(f"COD: {dados_veiculo['CodigoFipe']}")
            #print(f"Dados do veiculo: {dados_veiculo}" )
        else: 
            print("Classe Modelo com defeito"), resposta.status_code

#Classe que define um iterador Genérico
class Iterador:
    def __init__(self, dados):
        self.indice = 0
        self.dados = dados
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice < len(self.dados):
            dadoAtual = self.dados[self.indice]
            self.indice += 1
            return dadoAtual
        else:
            raise StopIteration