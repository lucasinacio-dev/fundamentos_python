# Autor: Lucas Inácio
# Projeto - Acesso do Usuário

idade = int(input("Qual sua idade: "))
credencial = input("Você tem a credencial (S/N): ")

# AND - Ambas as condições devem ser verdadeiras
# Para que o resultado seja verdadeiro
if idade >= 18 and credencial == "S":
    print("Acesso permitido!")
else:
    print("Acesso negado!")