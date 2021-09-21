class Conta:
    def __init__(self, cliente, saldo, limite):
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite

    def sacar(self, quantia):
        if (self.saldo - quantia) > 0:
            print(f"Retirando R${quantia} do saldo. Saldo antes do saque: R${self.saldo}.")
            self.saldo -= quantia
            print(f"Saldo após o saque: R${self.saldo}")
        else:
            print("Operação negada! Seu saldo ficaria menor que R$0!")

    def depositar(self, quantia):
        if (self.saldo + quantia) < self.limite:
            print(f"Adicionando R${quantia} ao seu saldo. Saldo antes do depósito: R${self.saldo}")
            self.saldo += quantia
            print(f"Saldo após o depósito: R${self.saldo}")
        else:
            print(f"Operação negada! Seu saldo ficaria maior que seu limite de R${self.limite}!")

    def consultar_saldo(self):
        print(f"O saldo do cliente {self.cliente} é de R${self.saldo}")
