class Funcionario:
    def __init__(self, nome, email, salario):
        self.nome = nome
        self.email = email
        self.salario = salario

    def solicitar_aumento(self):
        while True:
            try:
                aumento = float(input("Por favor, digite quanto você quer de aumento: "))
                if aumento > 0:
                    salario_atualizado = (self.salario * (aumento/100)) + self.salario
                    print(f"{self.nome}, seu pedido de aumento ao salário atual será enviado ao {self.email} do seu gerente. "
                          f"Caso seja aprovado, o salário R$ {self.salario:.2f} passará a ser de R$ {salario_atualizado}.")
                else:
                    print("")
                    print("ERRO!")
                    print("Programa encerrado")
                break
            except ValueError:
                print("")
                print("ERRO!")
                print("Programa encerrado")
                break

colaborador1 = Funcionario("Mateus","mateus@email.com.br", 3000)
colaborador1.solicitar_aumento()

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, senha_mestra):
        super().__init__(nome, email, salario)
        self.senha_mestra = senha_mestra

    def liberar_bonus(self):
        while True:
            try:
                acesso = input("Digite a senha mestra: ")
                if acesso == self.senha_mestra:
                    bonus = float(input("Digite um valor bônus para ser acrescentado ao salário: "))
                    if bonus > 0:
                        salario_com_bonus = self.salario + bonus 
                        print(f"{self.nome}, seu pedido de aumento ao salário atual será enviado ao {self.email} do diretor regional. "
                        f"Caso seja aprovado, o salário R$ {self.salario:.2f} passará a ser de R$ {salario_com_bonus}.")
                    break
                else:
                    print("Acesso negado!"
                          "Ligando para a polícia...")
            except ValueError:
                print("Digite um número!")

supervisor = Gerente("Adélio","só_cobra@mais_trabalho.com.br", 15000, "teste")
supervisor.liberar_bonus()
                
