
class Pessoa{
    constructor(name){
        this.name = name
    }
}

const lista = [new Pessoa('Mateus'),new Pessoa('Amanda'),new Pessoa('Fuefa'),new Pessoa('Gustavo')]

const listaNomes = lista.map((element => element.name))

console.log(listaNomes)