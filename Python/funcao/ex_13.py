# 🪄 Exercício: Grimório da Frieren
# Crie um def que receba 3 parâmetros e decida se a Frieren vai comprar o grimório ou continuar a viagem.
# Parâmetros:
# meses (Int): Tempo para decifrar.
# ouro (Int): Preço do livro.
# tipo (String): Efeito da magia.

# Critérios de REJEIÇÃO (Basta um ser verdadeiro):
# meses maior que 24 (Fern briga).
# ouro maior que 50 (Stark passa fome).
# tipo igual a "Combate" ou "Utilidade Pública" (Frieren só quer magia boba).

# Retorno:
# Uma tupla: (Decisao, Lista_de_Objeccoes).

def grimorio (meses,ouro,tipo):
    objecao = []
    if meses > 24:
        print("Fern fica emburrada")
        objecao.append(meses)
    else:
        print("Fern se conforma")
        
    if ouro > 50:
        print("Stark não tem energia pra servir de isca.")
        objecao.append(ouro)
    else:
        print("Stark consegue lutar e correr.")
        
    
    if tipo == "utilidade publica":
        print("Frieren compra!")
    else:
        print("Frieren recusa")
        objecao.append(tipo)

    if len(objecao) == 0:
        status = "COMPRAR GRIMÓRIO!"
    else:
        status = "CONTINUAR VIAGEM (RECUSADO)!"

    return objecao, status

while True:
    try:
        tempo = int(input("Quantos meses a Frieren pretende ficar no lugar: "))
        if tempo >= 0:
            break
        else:
            print("Sem magia de tempo negativo!")
    except ValueError:
        print("Sem magia de trocar números por letras!")

while True:
    try:
        dinheiros = float(input("Quanto a Frieren pretende gastar: "))
        if dinheiros > 0:
            break
        else:
            print("Assim a Frieren vai passar um século na prisão")
    except ValueError:
        print("Sem magia de trocar números por letras!")

tipo_magia = input("Digite o tipo da magia (utilidade publica/combate): ")
tipo_magia = tipo_magia.lower()

lista_de_erros, veredito = grimorio(tempo, dinheiros, tipo_magia)
print("\n" + "="*10 + " DIÁRIO DE VIAGEM " + "="*10)
print(f"STATUS FINAL: {veredito}")

if len(lista_de_erros) > 0:
    print(f"⚠️  Problemas encontrados: {', '.join(map(str, lista_de_erros))}")
print("="*38)
