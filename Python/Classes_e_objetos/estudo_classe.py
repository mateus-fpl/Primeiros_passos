class Anime:
    def __init__(self, titulo, protagonista, genero, ano_de_lancamento, poder):
        self.titulo = titulo
        self.protagonista = protagonista
        self.genero = genero
        self.ano_de_lancamento = ano_de_lancamento
        self.poder = poder

    def atacar(self):
        print(f"O personagem {self.protagonista} usou o golpe {self.poder}")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

p1 = Anime("Dragon Ball", "Goku", "Ação/Aventura", 1984, "KAMEHAMEHAAA")
p2 = Anime("Naruto", "Naruto", "Comédia/Aventura", 1999, "Rasengan")
p3 = Anime("Demon Slayer", "Tanjiro", "Drama/Aventura", 2019, "Hinokami Kagura")


print(p1)
print(p2)
print(p3)

p1.atacar()
p3.atacar()