class Sasageyo:
    def __init__(self, vida_eren, gas_da_tropa, poder_de_ataque_da_tropa, integridade_muralha):
        self.vida_eren = vida_eren
        self.gas_da_tropa = gas_da_tropa
        self.podataque_da_tropa = poder_de_ataque_da_tropa
        self.integridade_muralha = integridade_muralha

    def selar_a_brecha(self):
        self.integridade_muralha = self.integridade_muralha + 25
        self.vida_eren = self.vida_eren - 50 

    def ataque_distracao(self, titan_alvo):
        titan_alvo.vida_titan = titan_alvo.vida_titan - 300
        self.gas_da_tropa = self.gas_da_tropa - 15

    def recuperar_folego(self):
        self.vida_eren = self.vida_eren + 40

class Bestial:
    def __init__(self, vida_titan, poder_de_ataque_bestial):
        self.vida_titan = vida_titan
        self.poder_de_ataque_bestial = poder_de_ataque_bestial

    def acao_do_bestial(self, alvo_tropa):
        alvo_tropa.vida_eren = alvo_tropa.vida_eren - self.poder_de_ataque_bestial
        alvo_tropa.integridade_muralha = alvo_tropa.integridade_muralha - 10


tropa = Sasageyo(1000, 150, 300, 50)
macaco = Bestial(1000, 150)

print("------------ Contra-ataque da humanidade ------------\n")

while tropa.vida_eren > 0 and macaco.vida_titan > 0:
    print(f"Status - Eren: {tropa.vida_eren} HP | Gás: {tropa.gas_da_tropa} | Muralha: {tropa.integridade_muralha}% | Bestial: {macaco.vida_titan} HP")
    
    opcao = int(input("1 - Selar Brecha | 2 - Ataque Distração | 3 - Recuperar Fôlego\nDigite uma opção: "))
    
    match opcao:
        case 1:
            tropa.selar_a_brecha()
            macaco.acao_do_bestial(tropa)
        case 2:
            tropa.ataque_distracao(macaco) 
            macaco.acao_do_bestial(tropa)
        case 3:
            tropa.recuperar_folego()
            macaco.acao_do_bestial(tropa)
        case _:
            print("Opção inválida! Jogue outra vez.")
            continue 
            
    print("-" * 50)

if macaco.vida_titan <= 0:
    print("Vitória! O Titã Bestial foi derrotado!")
else:
    print("Derrota! A humanidade pereceu...")