pokedex = []
hp_pokemon = []
ataque_pokemon = []

for i in range (2):
    linha_pokedex = []
    linha_hp = []
    linha_ataque = []
    for j in range (2):
        pokemon = input(f"Digite o seu pokemon: ")
        hp_bichinho = int(input(f"Digite o HP do {pokemon}: "))
        poder_de_ataque = int(input(f"Digite o poder de ataque do {pokemon}: "))
        linha_pokedex.append(pokemon)
        linha_hp.append(hp_bichinho)
        linha_ataque.append(poder_de_ataque)
    pokedex.append(linha_pokedex)
    hp_pokemon.append(linha_hp)
    ataque_pokemon.append(linha_ataque)
    print(f"{pokemon} possui {hp_bichinho} HP com ataque de {poder_de_ataque} pontos.")


class Pokemon:
    def __init__(self, nome, hp, ataque):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome}")

    def receber_dano(self,alvo):
        self.hp = self.hp - alvo.ataque
        print(f"{self.nome} recebeu um ataque de {alvo.nome} e perdeu {alvo.ataque} de HP")
        print(f"HP restantes: {self.hp}")

poke1 = Pokemon(pokedex[0][0],hp_pokemon[0][0],ataque_pokemon[0][0])
poke2 = Pokemon(pokedex[0][0],hp_pokemon[0][0],ataque_pokemon[0][0])
poke1.atacar(poke2)
poke2.receber_dano(poke1)
