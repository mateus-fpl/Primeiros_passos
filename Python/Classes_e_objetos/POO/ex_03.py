class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_saldo(self):
        print(f"Seu saldo é R$ {self.saldo}.")

    def sacar(self):
        while True:
            try:
                saque = float(input("Digite um valor para saque: "))
                if saque > 0:
                    if saque <= self.saldo:
                        self.saldo = self.saldo - saque
                        print(f"Saldo restante: R$ {self.saldo}")
                        break
                    else:
                        print(f"Quantia maior que o saldo existente. R$ {self.saldo}")
                else:
                    print("Valor precisa ser maior que zero")
            except ValueError:
                print("Apenas números são aceitos. \nPor favor, digite novamente\n"
                "")

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite_cheque_especial):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self):
        while True:
            try:
                saque = float(input("Digite um valor para saque: "))
                if saque > 0:
                    if saque <= self.saldo + self.limite_cheque_especial:
                        self.saldo = self.saldo - saque
                        print(f"Saldo restante: R$ {self.saldo}")
                        break
                    else:
                        print(f"Quantia maior que o saldo existente. R$ {self.saldo}")
                else:
                    print("Valor precisa ser maior que zero")
            except ValueError:
                print("Apenas números são aceitos. \nPor favor, digite novamente\n"
                "")

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self):
            while True:
                try:
                    saque = float(input("Digite um valor para saque: "))
                    if saque > 0:
                        if saque <= self.saldo:
                            self.saldo = self.saldo - saque - 2
                            if self.saldo >= 0:
                                print(f"Saldo restante: R$ {self.saldo}")
                            else:
                                print("ERRO! Faltam os R$ 2.00 da taxa.")
                            break
                        else:
                            print(f"Quantia maior que o saldo existente. R$ {self.saldo}")
                    else:
                        print("Valor precisa ser maior que zero")
                except ValueError:
                    print("Apenas números são aceitos. \n Por favor, digite novamente\n"
                    "")



cliente1 = ContaCorrente("Mateus", 100, 500)
cliente1.sacar()


cliente2 = ContaPoupanca("Mateus",100)
cliente2.sacar()