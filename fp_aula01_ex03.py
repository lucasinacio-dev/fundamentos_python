# Autor: Lucas Inácio
# Projeto Calculadora com recebimento de dados

# Variável do tipo int é relativa a valores inteiros
# A palavra reservada input é usada para recever dados do usuário
valor1 = int (input('Digite o primeiro valor: '))
valor2 = int (input('Digite o segundo valor: '))
soma = valor1 + valor2
print(soma)

# Para gerar um print com texto, preciso que o texto esteja entre aspas
print('O resultado da soma é: ', soma)

# Print formatado usando f-string
print(f'O resultado da soma é: {soma}')