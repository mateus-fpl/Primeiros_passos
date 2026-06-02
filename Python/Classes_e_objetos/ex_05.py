# Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
# com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numero_conta, titular_conta, saldo_cliente=0):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo_cliente = saldo_cliente
    
    def alterarNome (self, novo_nome):
        self.titular_conta = novo_nome

    def deposito(self,valor):
        self.saldo_cliente += valor

    def saque(self, valor):
        if self.saldo_cliente >= valor:
            self.saldo_cliente -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Você não tem esse valor. Vai um empréstimo com juros abusivos?")
        

conta = int(input("Por favor, digite o número da sua conta: "))
cliente = input("Por favor, digite o seu nome: ")
saldo = float(input("Por favor, digite o seu saldo: "))

cliente_banco = ContaCorrente(conta, cliente, saldo)

print("Escolha uma opção (1 - sacar, 2 - depositar, 3 - sair)")
opcao = input(" ")

match opcao:
    case "1":
        print("Você escolher sacar")
        valor_saque = float(input("Quanto você gostaria de sacar? "))
        cliente_banco.saque(valor_saque)
        print(f"Caro cliente {cliente_banco.titular_conta}, seu saldo em sua conta {cliente_banco.numero_conta} é de {cliente_banco.saldo_cliente}R$.")

    case "2":
        print("Você escolher depositar")
        valor_deposito = float(input("Quanto você gostaria de depositar? "))
        cliente_banco.deposito(valor_deposito)
        print(f"Caro cliente {cliente_banco.titular_conta}, seu saldo em sua conta {cliente_banco.numero_conta} é de {cliente_banco.saldo_cliente}R$.")

    case "3":
        print("Você escolher sair:")
        print(f"Caro cliente {cliente_banco.titular_conta}, seu saldo em sua conta {cliente_banco.numero_conta} é de {cliente_banco.saldo_cliente}R$.")


