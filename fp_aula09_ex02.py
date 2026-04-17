# Autor: Lucas Inácio
# API - Conversor de Real para Dólar

import requests

valor_real = float(input('Digite o valor em reais (R$): '))

print('1 - Dólar')
print('2 - Euro')
opcao = input('Escolha a moeda: ')

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL'
resposta = requests.get(url)
dados = resposta.json()

if opcao == '1':
    cotacao = float(dados['USDBRL']['bid'])
    valor_convertido = valor_real / cotacao

    print(f'Cotação do dólar: R${cotacao:.2f}')
    print(f'Convertido em dólar: US${valor_convertido:.2f}')

else:
    cotacao = float(dados['EURBRL']['bid'])
    valor_convertido = valor_real / cotacao

    print(f'Cotação do euro: R${cotacao:.2f}')
    print(f'Convertido em euro: €{valor_convertido:.2f}')