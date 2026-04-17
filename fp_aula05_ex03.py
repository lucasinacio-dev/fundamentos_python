# Autor: Lucas Inácio
# Cálculo do fatorial de um número usando o loop FOR

numero = int(input("Digite um número: "))
fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i
    print(f"Fatorial parcial: {fatorial}")

print(f"Fatorial de {numero} é: {fatorial}")