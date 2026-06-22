#Considere uma equação do segundo grau, representada pela expressão Construa um programa no qual o usuário 
# informe os valores das constantes a, b e c. 
# Ao fim, o programa deve calcular e imprimir o valor de . Sabe-se que Δ =b2-4ac.

import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Equação inválida:")
else:
    delta = (b**2) - 4 * a * c
    if delta < 0:
        print("A equação não possui raízes.")
    else:
        raiz_delta = math.sqrt(delta)
        x = (-b + raiz_delta)/2*a
        x_2 = (-b - raiz_delta)/2*a

        print(f"O valor de x é: {x:.2f}\n O valor do outro x é: {x_2:.2f}")