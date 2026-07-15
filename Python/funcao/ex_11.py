# Um software de visão computacional acoplado ao microscópio analisa as lâminas de fezes de um paciente e gera um 
# relatório em texto para cada campo analisado.
# Se o microscópio encontrar a palavra "Negativo", o campo está limpo. Se encontrar qualquer outra palavra 
# (ex: "Giardia", "Ascaris", "Ameba"), significa que o paciente está parasitado.

# Crie uma função chamada analisar_laudo_parasitas. Ela deve receber uma lista contendo os resultados de cada 
# lâmina analisada do paciente (ex: ["Negativo", "Giardia", "Negativo"]). A função deve processar essa lista e 
# retornar uma tupla com duas informações:
# Um diagnóstico final (string): Se pelo menos uma lâmina contiver um parasita, o diagnóstico é "POSITIVO: 
# PACIENTE INFECTADO". Se todas estiverem limpas, o diagnóstico é "NEGATIVO".
# Uma nova lista contendo apenas os nomes dos parasitas encontrados (sem repetir o mesmo parasita se ele aparecer 
# em mais de uma lâmina).

# No programa principal:
# Pergunte ao usuário quantas lâminas foram preparadas para aquele paciente. Monte o loop para coletar os resultados
# de cada lâmina. 

def analisar_laudo_parasitas(lista_parasitas=None):
    if lista_parasitas is None:
        lista_parasitas = []
    if len(lista_parasitas) == 0:
        return "EXAME NEGATIVO", []
    
    lamina_positiva = []
    diagnostico = "NEGATIVO"


    for parasita in lista_parasitas:
        if parasita != "Negativo":
            diagnostico = "POSITIVO: PACIENTE INFECTADO"

        if parasita not in lamina_positiva:
                lamina_positiva.append(parasita)

    return diagnostico, lamina_positiva

laminas = []

while True:
    try:
        qtde_laminas = int(input("Digite quantas lâminas serão analisadas: "))
        if qtde_laminas > 0:
            break
    except ValueError:
        print("Apenas números inteiros e positivos são aceitos.\nDigite outra vez.\n")

for i in range (qtde_laminas):
    leitura_lamina = input(f"Digite o resultado da {i+1}º lâmina: ")
    leitura_lamina = leitura_lamina.strip().capitalize()
    laminas.append(leitura_lamina)

status_final, parasitas_achados = analisar_laudo_parasitas(laminas)

print("\n------- Resultado das leituras -------")
print(f"Resultado das lâminas: {laminas}")
print(f"Diagnóstico final: {status_final}")
print(f"Os parasitas encontrados foram: {parasitas_achados}")