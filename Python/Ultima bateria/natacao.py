#Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. Para isso, 
# eles convocaram os 7 melhores tempos da última competição e marcaram o tempo de cada um dos nadadores, na prova 
# dos 25 metros, estilo livre.
# Considerando que não houve tempos iguais, construa um programa que leia o nome e o tempo (em segundos) 
# de cada atleta e, em seguida, gere o seguinte relatório:
# a. nome do nadador com o melhor tempo
# b. nome do nadador com o pior desempenho
# c. tempo médio dos nadadores e
# d. quantidade de atletas com o tempo entre 12s e 15s

atletas = []
tempo = []
j = 0

while True:
    try:
       n = int(input("Quantidade de atletas participantes: "))
       break 
    except ValueError:
        print("Por favor, digite apenas um número inteiro!")
    

    
for i in range (n):
    competidor = input(f"Digite o nome do {i+1}º competidor: ")
    while True:
        try:
            segundos = float(input(f"Por favor, digite o tempo do {competidor}: "))
            break
        except ValueError:
            print("Apenas valores númericos são aceitos!")
    if segundos > 11 and segundos < 16:
        for j in range (i):
            j += 1
        
    
    atletas.append(competidor)
    tempo.append(segundos)
    quantidade_tempo_estimado = j

melhor_tempo = min(tempo)
pior_tempo = max(tempo)
media = sum(tempo)/len(tempo)


indice_melhor = tempo.index(melhor_tempo)
indice_pior = tempo.index(pior_tempo)

atleta_melhor = atletas[indice_melhor]
atleta_pior = atletas[indice_pior]

print("---------- Dados do Treino ----------")
print(" ")
print(f"O atleta com o melhor tempo foi {atleta_melhor} com {melhor_tempo} segundos.")
print(f"O atleta com o pior tempo foi {atleta_pior} com {pior_tempo} segundos.")
print(f"A média dos tempos dos {n} competidores foi {media:.2f} segundos.")
print(f"O número de atletas que ficou entre 12 e 15 segundos foi/foram: {quantidade_tempo_estimado}.")