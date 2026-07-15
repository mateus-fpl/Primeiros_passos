# Crie uma função chamada calcular_desconto. Ela deve receber dois parâmetros: o preco original de um produto e a 
# porcentagem de desconto que ele vai ganhar. A função deve calcular o valor do desconto e retornar o preço final 
# do produto já com o desconto aplicado.
# Fora da função (no seu programa principal), chame a função passando um produto de R$ 100 com 15% de desconto e 
# printe o resultado na tela.

def calcular_desconto(preco,porcentagem_desconto):
   desconto = (preco * porcentagem_desconto)/100
   return preco - desconto

while True:
    try:
        preco_produto = float(input("Digite o preço do produto: "))
        desconto_produto = float(input("Digite o valor de desconto do produto: "))
        if preco_produto > 0 and desconto_produto > 0:
            preco_final = calcular_desconto(preco_produto,desconto_produto)
            break
        else:
            print("Digite um valor válido!")
    except ValueError:
        print("Reiniciando cadastro...")
        print(" ")

print(f"O preço do produto com desconto é R$ {preco_final:.2f}")