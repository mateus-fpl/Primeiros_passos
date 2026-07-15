# Você precisa monitorar a temperatura de um freezer de armazenamento de enzimas e reagentes de PCR. 
# A temperatura ideal de operação é de -20°C. Se a temperatura subir para -15°C ou mais, o sistema deve disparar 
# um alerta de "PERIGO" (risco de perda de material). Se estiver abaixo de -15°C, está "OK".

# Crie uma função chamada verificar_freezer. Ela deve receber uma lista contendo as leituras de temperatura 
# registradas pelo sensor nas últimas horas (números decimais ou inteiros, ex: [-21.5, -19.0, -14.2]).
# A função deve processar essa lista e retornar uma tupla com duas informações:Uma string com o Status Geral do 
# lote: se pelo menos uma leitura atingiu o nível de perigo (> -15), o status geral é 
# "ALERTA: VERIFICAR MATERIAL". Caso contrário, o status é "SISTEMA ESTÁVEL".Uma nova lista contendo apenas as 
# temperaturas que ficaram na faixa de perigo.No programa principal:Pergunte ao usuário quantas leituras o sensor 
# coletou no turno.Monte o loop para coletar essas temperaturas (aceita números negativos e decimais). Dica de 
# validação: No laboratório, se o sensor marcar algo bizarro como acima de 15°C positivo ou abaixo de -50°C, 
# avise que é um "Erro de Leitura do Sensor" e peça para digitar aquela leitura novamente.Chame a função 
# passando a lista de temperaturas.Mostre o relatório final na tela.

def verificar_freezer(lista_temperatura=None):
    if lista_temperatura is None:
        lista_temperatura = []
    if len(lista_temperatura) == 0:
        return "SEM DADOS", []
    
    tempereraturas_perigosas_armazenadas = []
    status_geral = "SISTEMA ESTÁVEL"
  
    

    for temperaturas in lista_temperatura:
        if temperaturas >= - 15:
            status_geral = "ALERTA: VERIFICAR MATERIAL"
            tempereraturas_perigosas_armazenadas.append(temperaturas) 
    
    return status_geral, tempereraturas_perigosas_armazenadas

lista_temperaturas = []


while True:
    try:
        registro_no_seu_turno = int(input("Coloque quantas temperaturas foram registradas no seu turno: "))
        if registro_no_seu_turno > 0:
            break
        else:
            print("A contagem só pode ser positiva.")
            print("")
    except ValueError:
        print("Apenas números inteiros são aceitos!\nDigite um novo valor.")
        print("")

for i in range (registro_no_seu_turno):
    while True:
        try:
            registro_temperatura = float(input(f"Digite a {i+1}º temperatura: "))
            if -50 <= registro_temperatura <= 15:
                lista_temperaturas.append(registro_temperatura)
                break
            else:
                print("Erro de leitura do sensor. Digite a temperatura novamente.")
                break
        except ValueError:
            print("Apenas números são aceitos!")
            print(" ")

status_final, as_perigosas = verificar_freezer(lista_temperaturas)

print("\n--- RELATÓRIO DE BIOSSEGURANÇA ---")
print(f"Status do Lote: {status_final}")
print(f"Temperaturas que geraram risco aos reagentes: {as_perigosas}")




