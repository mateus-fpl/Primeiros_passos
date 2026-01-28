#Tô criando a classe
class planeta:
    def __init__(self, pais, capital, continente, hemisferio):
        self.pais = pais
        self.capital = capital
        self.continente = continente
        self.hemisferio = hemisferio
    
    #objeto pra só dar print ao invés de puxar a variável com o objeto.
    def __str__(self):
        return f"O {self.pais} cuja a capital é {self.capital} fica no {self.continente}, no {self.hemisferio}"


class America_do_Sul(planeta):
    def __init__(self, pais, capital, continente, hemisferio,idioma):
        super().__init__(pais, capital, continente, hemisferio)

        self.idioma = idioma

    def __str__(self):
        return f"O {self.pais} cuja a capital é {self.capital} fica no {self.continente} e seu idioma é {self.idioma}"

#Instanciando a classe filha com o acréscimo de idioma
p1 = America_do_Sul("Brasil", "Brasília", "América do Sul", "sul", "português")
p2 = America_do_Sul("Argentina", "Buenos Aires", "América do Sul", "sul", "espanhol")
p3 = America_do_Sul("Uruguai", "Montevidéu", "América do Sul", "sul", "espanhol")
p4 = America_do_Sul("Paraguai", "Assunção", "América do Sul", "sul", "espanhol e guarani")
p5 = America_do_Sul("Chile", "Santiago", "América do Sul", "sul", "espanhol")
p6 = America_do_Sul("Bolívia", "Sucre", "América do Sul", "sul", "espanhol, quíchua e aimará")
p7 = America_do_Sul("Peru", "Lima", "América do Sul", "sul", "espanhol e quíchua")
p8 = America_do_Sul("Equador", "Quito", "América do Sul", "norte/sul", "espanhol")
p9 = America_do_Sul("Colômbia", "Bogotá", "América do Sul", "norte", "espanhol")
p10 = America_do_Sul("Venezuela", "Caracas", "América do Sul", "norte", "espanhol")
p11 = America_do_Sul("Guiana", "Georgetown", "América do Sul", "norte", "inglês")
p12 = America_do_Sul("Suriname", "Paramaribo", "América do Sul", "norte", "holandês")
p13 = America_do_Sul("Guiana Francesa", "Caiena", "América do Sul", "norte", "francês")  

#Transformando os países em um array pra fazer um único print pelo join
paises = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]

print("Países do continente sul americano:\n")
print("\n".join(map(str,paises)))
print("\n")
#Mais uma classe filha
class Europa(planeta):
    def __init__(self, pais, capital, continente, hemisferio, moeda):
        super().__init__(pais, capital, continente, hemisferio)
        self.moeda = moeda
    
    def __str__(self):
        return f"O {self.pais} cuja a capital é {self.capital} fica no {self.continente} e sua moeda é {self.moeda}"
    
#Instanciando a classe filha Europa com o acréscimo de moeda
e1 = Europa("Alemanha", "Berlim", "Europa", "norte", "Euro")
e2 = Europa("França", "Paris", "Europa", "norte", "Euro")
e3 = Europa("Áustria", "Viena", "Europa", "norte", "Euro")
e4 = Europa("Bélgica", "Bruxelas", "Europa", "norte", "Euro")
e5 = Europa("Holanda", "Amsterdã", "Europa", "norte", "Euro")
e6 = Europa("Luxemburgo", "Luxemburgo", "Europa", "norte", "Euro")
e7 = Europa("Suíça", "Berna", "Europa", "norte", "Franco Suíço")
e8 = Europa("Liechtenstein", "Vaduz", "Europa", "norte", "Franco Suíço")
e9 = Europa("Mônaco", "Mônaco", "Europa", "norte", "Euro")

paises_europa = [e1,e2,e3,e4,e5,e6,e7,e8,e9]

print("Países do continente europeu: \n")
print("\n".join(map(str,paises_europa)))