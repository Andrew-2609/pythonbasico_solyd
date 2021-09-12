print("### Início do Programa ###\n")

quantidade = int(input("Por favor, insira a quantidade de convidados para a festa: "))
lista_convidados = []

for indice in range(0, quantidade):
    lista_convidados.append(input("Qual o nome do convidado " + str(indice + 1) + "?\n"))

print("\n## Exibindo a lista de convidados:\n")

for convidado in lista_convidados:
    print(convidado)

print("\n# Fim #\n")
