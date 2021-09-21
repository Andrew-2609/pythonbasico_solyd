from cliente import Cliente
from conta import Conta

cliente_andrew = Cliente("Andrew Monteiro", "111.222.333-44", 18)
conta_andrew = Conta(cliente_andrew, 0, 50)
cliente_joao = Cliente("João Vieira", "555.666.777-88", 20)
conta_joao = Conta(cliente_joao, 250, 500)

print(f"Dados da conta do cliente {conta_andrew.cliente.nome}:\n")
print(conta_andrew.consultar_saldo())
print(f"Seu limite atual: R${conta_andrew.limite}.")
conta_andrew.depositar(50)
conta_andrew.sacar(50)
conta_andrew.depositar(51)
conta_andrew.sacar(1)

print("\n---\n")

print(f"Dados da conta do cliente {conta_joao.cliente.nome}:\n")
print(conta_joao.consultar_saldo())
print(f"Seu limite atual: R${conta_joao.limite}.")
conta_joao.depositar(50)
conta_joao.sacar(600)
conta_joao.depositar(201)
