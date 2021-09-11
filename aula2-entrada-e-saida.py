print("### Formulário ###")

nome = input("Digite o seu nome: ")
cpf = input("Digite o seu CPF: ")
endereco = input("Digite o seu endereço: ")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura (ex: 1.76): "))
telefone = input("Digite o seu telefone: ")

print("\n## Resultado ##\n")

print(nome, "tem", idade, "anos de idade e possui", altura, "de altura.")
print("Seu número de telefone é:", telefone + ",", "e seu número de CPF é:", cpf + ".")
print(nome, "mora no seguinte endereço:", endereco + ".")

print("\n# Fim #")
