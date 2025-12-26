class pessoa {
    nome
    idade
    anoDeNascimento

    constructor(nome,idade){
        this.nome = nome
        this.idade = idade
        this.anoDeNascimento = 2025 - idade
    }

    descrever (){
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}`)
    }
}

const mateus = new pessoa("Mateus", 33)
const amanda = new pessoa("Amanda", 34)

console.log(mateus)