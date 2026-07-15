# Você está desenvolvendo o backend de um sistema que analisa sequências de DNA para identificar mutações em um gene
#  específico (como o gene BRAF ou EGFR associado a oncologia), determinando se uma amostra é Selvagem (Normal) ou 
# Mutada.
# Uma sequência de DNA saudável desse gene deve conter obrigatoriamente a sequência de bases (o "primer/alvo"): 
# "ATGCT". Se a amostra não contiver essa sequência exata, ela é classificada como "Mutada". Se ela contiver, ela é 
# "Selvagem".

# Crie uma função chamada analisar_amostras. Ela deve receber um parâmetro: uma lista contendo strings com as 
# sequências de DNA coletadas das amostras do dia. Dentro da função, você deve processar a lista e retornar uma 
# tupla com três informações:

#   A quantidade total de amostras analisadas.
#   Uma nova lista contendo apenas as sequências que foram classificadas como "Mutada".
#   A porcentagem (%) de amostras mutadas em relação ao total analizado.

# Crie um loop blindado para coletar as sequências. Regra de validação: A sequência de DNA só pode aceitar letras 
# maiúsculas e, para ser válida, precisa ter pelo menos 8 caracteres (ex do que o usuário digita: "ATCGATGC" ou 
# "TTTATGCTAA"). Se digitar menor que 8, avise que a leitura do sequenciador falhou.
# Chame a função passando a lista de strings coletadas.
# Desembrulhe a tupla e exiba o relatório na tela: o total de exames, a lista das sequências que deram mutadas e a 
# taxa de mutação do lote formatada (ex: 25.0%).

def analisar_amostras(lista_genes=None):
    if lista_genes is None:
        lista_genes = []
    if len(lista_genes) == 0:
        return [],0, 0.0

    amostras_mutantes = []

    total_amostras_analisadas = len(lista_genes)
    
    for amostras in lista_genes:
        if "ATGCT" not in amostras:
            amostras_mutantes.append(amostras)

    porcentagem = (len(amostras_mutantes)/total_amostras_analisadas) * 100

    return total_amostras_analisadas, amostras_mutantes, porcentagem

while True:
    try:
        qtde_amostras = int(input("Digite quantas amostras serão analisadas: "))
        if qtde_amostras > 0:
            break
        else:
            print("Digite ao menos uma amostra!")
    except ValueError:
        print("Apenas números inteiros positivos são aceitos.")
        print("Digite novamente.")
        print(" ")


genoma = []

for i in range (qtde_amostras):
    genes = input(f"Digite o código da {i+1}º amostra: ").upper()
    if len(genes) < 8:
        print(f"Leitura da amostra {genes} muito curta!")
        print("Amostra invalidada e automaticamente excluída!")
    else:
        genoma.append(genes)

total, genes_mutados, taxa = analisar_amostras(genoma)

print("\n--- RELATÓRIO DO LOTE ---")
print(f"Total de amostras válidas analisadas: {total}")
print(f"Amostras que apresentaram mutação: {genes_mutados}")
print(f"Taxa de mutação do lote: {taxa:.1f}%")