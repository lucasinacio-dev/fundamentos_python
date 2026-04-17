# Autor: Lucas Inácio
# Array de 10 alunos
# 2 alunos desistiram
# 1 aluno entrou
# Ordenar em ordem alfabética

alunos = ['Lucas', 'Lorena', 'Nivaldo', 'Valdete', 'Mateus', 'Natália', 'Simone', 'Rodrigo', 'Wilson', 'Adriana']

del [alunos[0], alunos[6]]
print(alunos)

alunos.append('Amadeu')
print(alunos)

alunos.sort()
print(*alunos, sep=' | ')