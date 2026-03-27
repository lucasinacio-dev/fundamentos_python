# Autor: Lucas Inácio
# Projeto - Acesso do Usuário

usuario = input("Digite o nome do usuário: ")
senha = input("Digite a senha: ")

# AND - Ambas as condições devem ser verdadeiras
# Para que o resultado seja verdadeiro
if usuario == "admin" and senha == "1234":
    print("Acesso permitido!")
else:
    print("Acesso negado!")