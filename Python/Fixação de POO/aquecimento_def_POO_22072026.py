def processar_relatorio_combate():
    
    lista_herois = []
    lista_ameacas = []
    quantidade_pontos = []
    n = int(input("Digite a quantidade de herois: "))

    for i in range (n):
        heroi = input("Digite o nome do heroi: ")
        lista_herois.append(heroi)
        pontos = 0
        ameaca_derrotada = input("Digite a ameaça derrotada: ")
        danos_colaterais = input("Houve danos colaterais: ")
        match ameaca_derrotada:
            case "lobo":
                if danos_colaterais == "n":
                    pontos = pontos + 10
                else:
                    pontos = pontos - 20
            case "tigre":
                if danos_colaterais == "n":
                    pontos = pontos + 25
                else:
                    pontos = pontos - 20
            case "demonio":
                if danos_colaterais == "n":
                    pontos = pontos + 50
                else:
                    pontos = pontos - 20
            case "dragão":
                if danos_colaterais == "n":
                    pontos = pontos + 100
                else:
                    pontos = pontos - 20

        lista_ameacas.append(ameaca_derrotada)
        quantidade_pontos.append(pontos)
        total_pontos = sum(quantidade_pontos)
    return lista_herois, lista_ameacas, total_pontos

herois, ameacas, pontos = processar_relatorio_combate()

print("\n" + "="*40)
print("   RELATÓRIO DE COMBATE DA ASSOCIAÇÃO   ")
print("="*40)
# O .join() junta a lista inteira com vírgulas!
print(f"🦸 Heróis: {', '.join(herois)}")
print(f"👾 Ameaças Derrotadas: {', '.join(ameacas).title()}")
print(f"⭐ Pontuação Total: {pontos} pontos")
print("="*40)


        
