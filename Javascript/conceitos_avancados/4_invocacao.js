const pessoa = {
    nome: 'Mateus',
    idade: 33
}

function gritar(prefixo){
    console.log(prefixo, this.nome)
}

gritar.apply(pessoa, ['Olaaaaaaaa'])
gritar.call(pessoa, 'Olaaaaaa')



