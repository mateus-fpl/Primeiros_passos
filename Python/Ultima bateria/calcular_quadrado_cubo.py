# Construa um programa que receba um número inteiro positivo informado pelo usuário. 
# Caso ele seja par, o programa deve calcular o seu quadrado. Mas, se ele for ímpar, 
# deve ser calculado o seu cubo. Ao fim, o programa deve imprimir o valor calculado.

import math

numero = int(input("Por favor digite um número inteiro positivo: "))

while numero <= 0:
    print ("Número inválido!")
    numero = int(input("Por favor digite um número inteiro positivo: "))
    
if numero%2 == 0:
    resultado = math.pow(numero,2)
else:
    resultado = math.pow(numero,3)
  
print(f"O resultado do número {numero} é {resultado}")
