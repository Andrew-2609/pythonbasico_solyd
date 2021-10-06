import re

meu_regex = r"[\w.-]+@[\w-]+\.[\w.-]+"

lista_de_teste = ["ndrewcoding@ndog.com", "brazil.com", "jonathan.harker@gmail.com"]

padroes = re.findall(meu_regex, str(lista_de_teste))

if padroes:
    print(padroes)
else:
    print("Padrão não encontrado...")
