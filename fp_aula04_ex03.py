# Autor: Lucas Inácio
# Projeto - Acesso do Usuário

idade = (input("Você tem a carteira de motorista (S/N): "))
credencial = input("Você passou no teste de bafômetro (S/N): ")

# AND - Ambas as condições devem ser verdadeiras
# Para que o resultado seja verdadeiro
if idade == "S" and credencial == "S":
    print("Acesso permitido!")
else:
    print("Acesso negado!")