class quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def calcular_area (self):
        resultado = self.tamanho_do_lado * self.tamanho_do_lado
        return resultado
    
lado = quadrado(5)
print(f"O lado do quadrado é {lado.tamanho_do_lado} cm.")

valor_area = lado.calcular_area()
print(f"A área do quadrados é {valor_area} cm.")