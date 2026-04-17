# Autor: Lucas Inácio
# API - Previsão do Tempo

import requests

latitude = float(input('Digite sua latitude: '))
longitude = float(input('Digite sua longitude: '))

url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}2&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
resposta = requests.get(url)
dados = resposta.json()

print(f"Horário de leitura: {dados['current']['time']}")
print(f"Temperatura: {dados['current']['temperature_2m']}°C")
print(f"Velocidade do vento: {dados['current']['wind_speed_10m']} km/h")