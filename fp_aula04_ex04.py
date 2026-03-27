# Autor: Lucas Inácio
# Projeto - Uso de AND

idade = int(input("Digite sua idade: "))
bebida = input("Consumiu álcool (S/N): ")

if idade >= 18 and bebida != "S":
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")