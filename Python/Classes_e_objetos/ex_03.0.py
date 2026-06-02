class retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calculo_area(self):
        return self.lado_a * self.lado_b
        
    
    def calculo_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


    def novo_medida(self, novo_a, novo_b):
        self.lado_a = novo_a
        self.lado_b = novo_b

a = float(input("Digite a altura do local: "))
b = float(input("Digite a largura do local: "))

comodo = retangulo(a, b)

area = comodo.calculo_area()
perimetro = comodo.calculo_perimetro()

print(f"\nPara este local de {a}m x {b}m:")
print(f"Área (Pisos): {area} m²")
print(f"Perímetro (Rodapés): {perimetro} m")



    