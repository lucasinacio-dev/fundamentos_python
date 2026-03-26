# Autor: Lucas Inácio
# Solução para facilitar os trabalhos dos consultores - Upgrade no projeto

largura = float (input('Digite a largura do terreno: '))
comprimento = float (input('Digite o comprimento do terreno: '))
MetroQuadrado = 1000
area = largura * comprimento
ValorMetro = area * MetroQuadrado
print('A área do terreno é: ', area , 'E o valor é: ', ValorMetro)