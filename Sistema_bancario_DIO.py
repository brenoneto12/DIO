class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= 500 and len(self.saques) < 3:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque ou limite diário de saques atingido.")

    def extrato(self):
        print("Extrato:")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    banco = Banco()

    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            banco.depositar(valor)
        elif escolha == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            banco.sacar(valor)
        elif escolha == "3":
            banco.extrato()
        elif escolha == "4":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
