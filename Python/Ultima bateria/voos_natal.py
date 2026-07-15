# Construa um programa que cadastre diversos voos aéreos, bem como sua origem e seu destino. Considere o número do
#  voo como sendo a chave. Com base no que foi armazenado no dicionário, o programa deve informar a quantidade de 
# voos cuja origem é Natal.

voos = { '0001': {
        'origem': 'São Paulo',
        'destino': 'Rio de Janeiro'
        },

        '0002':{
            'origem': 'Natal',
            'destino': 'Rio de Janeiro'
        },

        '0003':{
            'origem': 'Olinda',
            'destino': 'Curitiba'

        },

        '0004':{
            'origem': 'Natal',
            'destino': 'Amapá'
        },

        '0005':{
            'origem': 'Natal',
            'destino': 'Recife'
        },

        '0006':{
            'origem': 'Natal',
            'destino': 'Paris'
        },

        '0007':{
            'origem': 'Teresina',
            'destino': 'Porto Velho'
        },

        '0008':{
            'origem': 'Rio de Janeiro',
            'destino': 'Natal'
        },

        '0009':{
            'origem': 'Belem',
            'destino': 'Recife'
        },

        '0010':{
            'origem': 'Natal',
            'destino': 'Salvador'
        }
}
voos_origem_natal = 0

for contador in voos:
    voos_para_natal = voos[contador]['origem']

    if voos_para_natal == 'Natal':
        voos_origem_natal +=1

print(f"A quantidade de vôos que saem de Natal é {voos_origem_natal}.")
print(" ")
print(" ")

voos_limpos = {}
# Com base no dicionário da questão anterior, construa um programa para remover os voos cujo destino é Recife. 
# Em seguida, imprima a nova listagem de voos.
print("A lista de vôo sem Recife é:")
for contador in voos:
    voos_exceto_recife = voos[contador]['destino']

    if voos_exceto_recife != 'Recife':
        voos_limpos[contador] = voos[contador]

for chave in voos_limpos:
    origem = voos_limpos[chave]['origem']
    destino = voos_limpos[chave]['destino']
    
    print(f"Voo: {chave} | Origem: {origem} | Destino: {destino}")

# Ainda com base no dicionário da questão 3, construa um programa em que, após os voos terem sido cadastrados, o 
# usuário possa modificar a origem e/ou o destino de um determinado voo. Ao fim, o programa deve imprimir a nova 
# listagem de voos.
print("")
codigo_alterar = input("Digite o código do vôo que você deseja alterar: ")

if codigo_alterar in voos:
    nova_origem = input("Digite a nova ORIGEM: ")
    novo_destino = input("Digite o novo DESTINO: ")

    voos[codigo_alterar]['origem'] = nova_origem
    voos[codigo_alterar]['destino'] = novo_destino
    
    print("\n Voo atualizado com sucesso!")
else:
    print("\n Voo não encontrado!")

for chave in voos:
    origem = voos[chave]['origem']
    destino = voos[chave]['destino']
    
    print(f"Voo: {chave} | Origem: {origem} | Destino: {destino}")
