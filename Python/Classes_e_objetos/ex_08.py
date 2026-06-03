# Desenvolva uma classe Macaco, que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(),
#  ver_bucho() e digerir().
# Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 
# 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um 
# macaco coma o outro. É possível criar um macaco canibal?

class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def rango(self, comer ):
        self.bucho.append(comer)

    def ver_bucho(self):
        print(f"Tudo que o macaco comeu foi {self.bucho}")

    def __str__(self):
        return self.nome
    
    def __repr__(self):
        return self.nome

    
macaco1 = Macaco("Adailton")
macaco2 = Macaco("Kleber")

macaco1.rango("banana")
macaco1.rango(macaco2)
macaco1.ver_bucho()