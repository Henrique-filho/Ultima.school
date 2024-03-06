#ATIVIDADE M4S1:
#ITERANDO DADOS DA API https://deividfortuna.github.io/fipe/ COLSULTANDO TIPOS DE VEICULOS DE UMA DETERMINADA MARCA.
import requests

from classes_consulta import TabelaFipe, Iterador

#Cria o objeto
consulta_fipe = TabelaFipe()

#Obtem as marcas de carros
marcas = consulta_fipe.obter_todas_marcas()
iteradorMarcas = Iterador(marcas)
for marca in iteradorMarcas:
    print(marca)

#Obtem os modelos de carros por marca
marca_id = input("Digite o ID da marca que deseja consultar: ")
modelos = consulta_fipe.obter_todos_modelos(marca_id)
iteradorModelos = Iterador(modelos)
for modelo in iteradorModelos:
    print(modelo)

#Obtem as informações de anos de um carro por modelo
modelo_id = input("Digite o ID do modelo que deseja consultar: ")
anos = consulta_fipe.obter_todos_anos(marca_id, modelo_id)
iteradorAnos = Iterador(anos)
for ano in iteradorAnos:
    print(ano)

#Obtem as informações de um carro de um ano escolhido
ano_id = input("Digite o ID do ano que deseja consultar: ")
info = consulta_fipe.obter_informacoes_veiculo(marca_id, modelo_id, ano_id)