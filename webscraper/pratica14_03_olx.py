
from requests_html import HTMLSession

sessao = HTMLSession()

url = "https://www.olx.com.br/imoveis/aluguel/estado-mt/regiao-de-rondonopolis-e-sinop"

resposta = sessao.get(url)

for link in resposta.html.find("#ad-list li a"):
    print(link.attrs['href'])