# ⚖️ Desafio: A Balança da Aura
# Crie uma função que compare a quantidade de Mana entre dois personagens. Quem tiver menos Mana obedece camente ao 
# que tem mais Mana (ou seja, perde o controle do próprio corpo).

import random
def qtde_de_mana(mana_aura, mana_frieren):
    
    mana_aura = random.randint(1, 1000000)
    mana_frieren = random.randint(1, 1000000)
    print(f"A mana da Aura é de {mana_frieren:}")
    print(f"A mana da Frieren é de {mana_aura:}")
    
    if mana_aura > mana_frieren:
            resultado_batalha = "Frieren, você agora me pertence."
            status_aura = "Aura vitoriosa!"
    else:
            resultado_batalha = "Aura, se mate agora."
            status_aura = "DERROTADA"

    return resultado_batalha, status_aura

print ("--------- Derrotem o demônio da balança! ---------")
mana_aura = random.randint(1,1000000)
mana_frieren = random.randint(1,1000000)
aura, frieren = qtde_de_mana(mana_aura, mana_frieren)
print("")
print("--------- Fim do combate ----------")
print(f"Nivel de mana da aura foi: {aura}")
print(f"Nivel da mana da Frieren foi: {frieren}")



