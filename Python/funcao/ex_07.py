# Crie uma função chamada calcular_media. Ela deve receber duas notas como parâmetros (ex: nota1 e nota2).
# Dentro dela, a função deve calcular a média aritmética simples dessas duas notas e retornar o resultado.
# No seu programa principal:
# Peça para o usuário digitar a Nota 1 e a Nota 2 (pode usar o seu validador try/except se quiser, ou fazer o input direto para ir mais rápido).
# Chame a função passando essas notas.
# Guarde o retorno em uma variável e printe na tela se o aluno passou ou não 
# (considere média maior ou igual a 6.0 para passar).

def calcular_media(lista_notas=None):
    if lista_notas is None: 
        lista_notas = []
    if len(lista_notas)==0:
        return 0
    media = sum(lista_notas)/len(lista_notas)
    return media

while True:
    try:
        qtde_avaliacao = int(input("Digite quantos avaliações foram feitas: "))
        if qtde_avaliacao > 0:
            print("Valor aceito")
            break
        else:
            print("Digite um número positivo!")
            
    except ValueError:
        print("Valor inválido! Reiniciando cadastro...")

notas =[]

for i in range (qtde_avaliacao):
    while True:
        try:
            nota = float(input(f"Digite a {i+1}º nota do(a) aluno(a):"))
            if nota >= 0 and nota <= 10:
                notas.append(nota)
                break
            else:
                print("Digite uma nota válida!")
        except ValueError:
                print("Apenas números!")

media_final = calcular_media(notas)
if media_final >= 7:
    print(f"Aluno aprovado! A média final do aluno foi: {media_final:.2f}")
elif media_final >= 5:
    print(f"Recuperação! A média final do aluno foi: {media_final:.2f}")
else:
    print(f"Aluno reprovado! A média final do aluno foi: {media_final:.2f}")



