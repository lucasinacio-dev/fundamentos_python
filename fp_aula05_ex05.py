# Autor: Lucas Inácio
# Se número for positivo (> que 0)
# Conte os números positivos
# Range de 10

contador_positivo = 0
contador_negativo = 0

for i in range(4):
    numero = int(input("Digite um número: "))
    print(f'Núm. dig: {numero} e o valor de i é {i}')
    if numero > 0:
        contador_positivo = contador_positivo + 1
    elif numero < 0:
        contador_negativo = contador_negativo + 1

print(f'Quantidade de números positivos: {contador_positivo}')
print(f'Quantidade de números negativos: {contador_negativo}')