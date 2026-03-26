# Autor: Lucas Inácio
# Projeto Cálculo da Hipotenusa
# Potência

oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (adjacente**2 + oposto**2) ** 0.5

# Exibir o número formatado com 2 casas decimais
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

#round()
hipotenusa = round(hipotenusa, 2)
print(f'O valor da hipotenusa é: {hipotenusa}')