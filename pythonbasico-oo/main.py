from veiculo import Veiculo

caminhao_rosa = Veiculo("rosa", 8, "ford", 10)

print("CAMINHÃO ROSA\n",
      f"Cor: {caminhao_rosa.cor}, número de rodas: {caminhao_rosa.rodas},"
      f" marca: {caminhao_rosa.marca}, tanque: {caminhao_rosa.tanque}")

print("")

carro_azul = Veiculo("azul", 4, "bmw", 30)

print("CARRO AZUL\n",
      f"Cor: {carro_azul.cor}, número de rodas: {carro_azul.rodas},"
      f" marca: {carro_azul.marca}, tanque: {carro_azul.tanque}")

carro_azul.abastecer(35)

print("Nova quantidade de litros no tanque do carro azul:", carro_azul.tanque)
