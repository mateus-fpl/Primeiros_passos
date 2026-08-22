def calcular_aura_absorvida(tipo_presa, forca_base, quantidade):
    if tipo_presa == "usuário de nen":
        aura = ((forca_base * 5) * quantidade)
        print(f"A rainha comeu {quantidade} da(s) criatura(s) tipo {tipo_presa}." 
              f"A força base da(s) criatura(s) era(m) de {forca_base}. Ela ganhou {aura} de aura")
    else:
        aura = (forca_base * quantidade)
        print(f"A rainha comeu {quantidade} da(s) criatura(s) tipo {tipo_presa}." 
            f"A força base da(s) criatura(s) era(m) de {forca_base}. Ela ganhou {aura} de aura")
    
    return aura

vitima = calcular_aura_absorvida("usuário de nen", 30, 6)
vitima2 = calcular_aura_absorvida("urso",30,6)

class FormigaQuimera:
    def __init__(self, nome, quantidade_aura):
        self.nome = nome
        self.quantidade_aura = quantidade_aura

    def atacar(self):
        print(f"{self.nome} realiza um ataque físico básico de formiga.")

class ComandanteDeDivisiao(FormigaQuimera):
    def __init__(self, nome, quantidade_aura):
        super().__init__(nome, quantidade_aura)

    def atacar(self):
        print(f"{self.nome} usa sua habilidade individual de Nen com {self.quantidade_aura} de poder!")

class GuardaReal(FormigaQuimera):
    def __init__(self, nome, quantidade_aura):
        super().__init__(nome, quantidade_aura)

    def atacar(self):
        print(f"{self.nome} desfere um golpe devastador da Guarda Real para proteger o Rei!")

    
soldado = FormigaQuimera("Rato", 20)
soldado.atacar()

lider = ComandanteDeDivisiao("Leo",200)
lider.atacar()

guarda = GuardaReal("Neferpitou", 5000)
guarda.atacar()