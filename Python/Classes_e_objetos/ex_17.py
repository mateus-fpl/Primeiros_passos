class Soldado:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def receber_dano(self, quantidade):
        self.quantidade = quantidade
        self.vida = self.vida - quantidade
        print(f"{self.nome} recebeu {self.quantidade} de dano! Vida restante: {self.vida}")

    def atacar(self, alvo):
        alvo.receber_dano(20)
        print(f"{self.nome} atacou {alvo.nome} com um golpe básico")


soldado1 = Soldado("Levi", 100)
soldado2 = Soldado("Gabi", 100)
soldado1.atacar(soldado2)
soldado2.atacar(soldado1)


class Defensor(Soldado):
    def __init__(self, nome, vida, escudo):
        super().__init__(nome, vida)
        self.escudo = escudo

    def receber_dano(self, quantidade):
        if quantidade <= self.escudo:
            self.escudo = self.escudo - quantidade
            print(f"{self.nome} absorveu todo o impacto! Escudo restante: {self.escudo}")
        else:
            dano_restante = quantidade - self.escudo
            self.escudo = 0
            self.vida = self.vida - dano_restante
            print(f"Escudo do {self.nome} FOI DESTRUIDO! {self.nome} recebeu {dano_restante} de dano na vida! Vida restante: {self.vida}.")


class Atirador(Soldado):
    def __init__(self, nome, vida, municao):
        super().__init__(nome, vida)
        self.municao = municao  

    def causar_dano(self, alvo):
        if self.municao > 0:
            dano_tiro = 30
            print(f"Tiro em cheio! {self.nome} causou {dano_tiro} de dano em {alvo.nome}!")
            self.municao -= 1
            alvo.receber_dano(dano_tiro)  
        else:
            dano_basico = 10
            print(f"{self.nome} está sem munição e atacou {alvo.nome} com a coronha da arma!")
            alvo.receber_dano(dano_basico)


soldado3 = Atirador("Sasha", 100, 3) 
soldado4 = Defensor("Reiner", 100, 30)

# A Sasha ataca o Reiner 4 vezes seguidas:
print("\n--- INÍCIO DO COMBATE: SASHA VS REINER ---")
soldado3.causar_dano(soldado4)  
soldado3.causar_dano(soldado4)  
soldado3.causar_dano(soldado4)  
soldado3.causar_dano(soldado4)  