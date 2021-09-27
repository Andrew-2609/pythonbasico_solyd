arquivo_de_escrita = open("arquivo_de_escrita.txt", 'w')

for i in range(1, 11):
    arquivo_de_escrita.write(f"Linha {i}\n")

arquivo_de_leitura = open("arquivo_de_leitura.txt", 'r')

for linha in arquivo_de_leitura:
    print(f"-> {linha}")
