# Autor: Lucas Inácio
# Cálculo do fatorial de um número usando o loop WHILE

# Usuário digitou 5
num = int(input("Digite um número: "))
fatorial = 1

# 5 4 3 2 1
while num > 0:
    # Fatorial 5! = 5*4*3*2*1
    fatorial = fatorial * num
    num = num - 1
    print(f'Variável num vale: {num} e o fatorial vale: {fatorial}')
print("Fatorial", fatorial)