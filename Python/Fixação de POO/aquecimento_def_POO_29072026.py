def calcular_dano_nen(nome,aura, forca, defendeu_com_ken):
    if defendeu_com_ken == True:
        dano = (aura*forca)/2
        print(f"{nome} tem {aura} de aura, força {forca} e seu ataque causou dano de {dano}")
    else:
        dano = aura * forca
        print(f"{nome} tem {aura} de aura, força {forca} e seu ataque causou dano de {dano}")

    return dano
    print(f"O lutador tem {aura} de aura, força {forca} e seu ataque causou dano de {dano}")

lutador = calcular_dano_nen("Gon",10,100,True)


class Lutador_do_200º_andar:
    def __init__(self, nome, tipo_nen, vitorias):
        self.nome = nome
        self.tipo_nen = tipo_nen
        self.vitorias = vitorias

    def registrar_vitoria(self):
        self.vitorias = self.vitorias + 1

    def historico(self):
        print(f"{self.nome} usa o nem tipo {self.tipo_nen} e está com {self.vitorias} vitórias")

novato = Lutador_do_200o_andar("Kurapika","especial",4)
novato.historico()
novato.registrar_vitoria()
novato.registrar_vitoria()
novato.registrar_vitoria()
novato.historico()