# Autor: Lucas Inácio
# Array de filmes

filmes = ['Alerta Vermelho', 'Vingadores', 'Capitão América', 'Homem de Ferro', 'Resgate Implácavel']

print(filmes[2])
filmes.append('John Wick')
print(filmes)
# Inserir filme na posição 2 - Anônimo
filmes.insert(2, 'Anônimo')
print(filmes)
# Listar em ordem alfabética
filmes.sort()
print(*filmes)
print(*filmes, sep=' | ')