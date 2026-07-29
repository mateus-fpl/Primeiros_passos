import random

def analisar_ki(nome_guerreiro,ki):
    if ki > 8000:
        print (f"É MAIS DE 8000! Como que alguém como {nome_guerreiro} pode ter esse nível?!")
    elif ki > 1000:
        print (f"{nome_guerreiro} tem um ki de {ki}. Talvez me divirta um pouco.")
    else:
        print(f"Verme insolente! Como ousa desafiar o príncipe dos sayajins com um ki tão baixo?! {nome_guerreiro}, irá pro inferno agora mesmo!")

guerreiro1 = analisar_ki("Yamcha", random.randint(1,10000))
guerreiro2 = analisar_ki("Picollo", random.randint(1,10000))
guerreiro3 = analisar_ki("Kurilin", random.randint(1,10000))
guerreiro4 = analisar_ki("Kakaroto", random.randint(1,10000))

class GuerreiroZ:
    def __init__(self, nome, nivel_base, nivel_atual):
        self.nome = nome
        self.nivel_base = nivel_base
        self.nivel_atual = nivel_atual


class SalaDoTempo:
    def __init__(self):
        pass

    def treinar_guerreiro(self, guerreiro_alvo):
        nivel_melhorado = random.randint(1,10)
        guerreiro_alvo.nivel_atual = guerreiro_alvo.nivel_atual * nivel_melhorado
        print(f"{guerreiro_alvo.nome} treinou na sala do Tempo e seu nível subiu para {guerreiro_alvo.nivel_atual}!")
        print(f"Novo nível de Ki: {guerreiro_alvo.nivel_atual}!\n")

boneco1 = GuerreiroZ("Trunks", 100, 100)
boneco1_treino = SalaDoTempo()
boneco1_treino.treinar_guerreiro(boneco1)
