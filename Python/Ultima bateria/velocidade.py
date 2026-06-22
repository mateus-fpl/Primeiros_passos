# Implemente um programa que converta o valor de uma velocidade média em km/h para m/s. 
# Para isso, o usuário deve informar o valor da velocidade média. Sabe-se que o fator 
# utilizado para essa conversão é 3,6.

variavel = input("Você gostaria de digitar a velocodade em km/h ou m/s: ")

if variavel == "km/h":
    velocidade = float(input("Digite a velocidade em km/h: "))
    metros_por_segundo = velocidade/3.6

    print(f"A velocidade {variavel} km/h convertida em metros por segundo é: {metros_por_segundo :.2f} m/s.")
else:
    velocidade = float(input("Digite a velocidade em km/h: "))
    quilometros_por_hora = velocidade*3.6

    print(f"A velocidade {velocidade} m/s convertido em km/h é: {quilometros_por_hora:.2f} km/h.")