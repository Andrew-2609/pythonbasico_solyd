print("### Início do programa ###\n")

idade = int(input("Informe sua idade: "))

if idade < 18:
    print("Para entrar no exército, você precisa ter pelo menos 18 (dezoito) anos de idade!")
    exit(0)

peso = float(input("Informe seu peso: "))

if peso < 60.0:
    print("Para entrar no exército, você precisa ter pelo menos 60 (sessenta) quilos!")
    exit(0)

altura = float(input("Informe sua altura (ex: 1.75): "))

if altura < 1.7:
    print("Para entrar no exército, você precisa ter pelo menos 1.70m (um metro e setenta centímetros) de altura!")
    exit(0)

print("\nParabéns, você está apto a entrar no exército!")

print("\n# Fim #")
