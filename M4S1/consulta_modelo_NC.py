#ATIVIDADE M4S1:
#ITERANDO DADOS DA API https://deividfortuna.github.io/fipe/ COLSULTANDO TIPOS DE VEICULOS DE UMA DETERMINADA MARCA.
import requests

from classes_consulta import Marca 
from classes_consulta import Veiculo
from classes_consulta import Fipe
from classes_consulta import Modelo

consulta_fipe = Marca()

marcas = consulta_fipe.obter_todas_marcas()
for marca in marcas:
    print(f"ID da Marca: {marca['codigo']} - Nome da Marca: {marca['nome']}")
        

selecionar_marca = input("Digite o ID da marca que deseja consultar:")
marca_selecionada = selecionar_marca
iterador = Fipe(marca_selecionada)

for modelo in iterador:
    print(f"ID: {modelo['ID']} - Nome: {modelo['NOME']}")

consulta = Modelo()
id_veiculo = input('Digite o ID do veículo desejado: ')
consulta.atributo_modelo(marca_selecionada, id_veiculo, )





