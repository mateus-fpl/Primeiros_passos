# def calcular_dano(tipo_ataque, tipo_defensor,dano_base):

#     if tipo_ataque == "fogo" and tipo_defensor == "planta":
#         dano_base = dano_base * 2
#     elif tipo_ataque == "planta" and tipo_defensor == "água":
#         dano_base = dano_base * 2
#     elif tipo_ataque == "água" and tipo_defensor == "fogo":
#         dano_base = dano_base * 2
#     elif tipo_ataque == tipo_defensor:
#         dano_base = dano_base * 0.5
#     else:
#         dano_base
#     return dano_base

# batalha1 = calcular_dano("fogo", "planta", 50)
# print(f"O total do dano foi {batalha1}")
# batalha2 = calcular_dano("água","água",40)
# print(f"O total do dano foi {batalha2}")
# batalha3 = calcular_dano("planta","fogo",60)
# print(f"O total do dano foi {batalha3}")        
    

class Pokemon:
    def __init__(self,nome_pokemon, vida_maxima, vida_atual):
        self.nome_pokemon = nome_pokemon
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima

    def receber_dano(self, quantidade):
        self.quantidade = quantidade
        self.vida_atual = self.vida_atual - quantidade
        print(f"Status atual do seu pokémon: {self.vida_atual} HP.")


class EnfermeiraJoy:
    def __init__(self):
        pass
    
    def curar_pokemon(self, pokemon_alvo):
        pokemon_alvo.vida_atual = pokemon_alvo.vida_maxima
        print(f"Bip-bip-bip! Seu {pokemon_alvo.nome_pokemon} foi totalmente curado!")


my_poke = Pokemon("Pikachu",100,100)
my_poke.receber_dano(20)
nurse_joy1 = EnfermeiraJoy()
nurse_joy1.curar_pokemon(my_poke)
