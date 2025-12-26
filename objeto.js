const pessoa = {
    nome: "Mateus Paes",
    idade: 33,
    descrever (){
        console.log(`Meu nome é ${this.nome} e minha idade é ${this.idade}. 
            Minha altura é ${this.altura} e meu peso é ${this.peso}`)
    }
}

pessoa.descrever = function(){
    console.log(`Meu nome é ${this.nome}`)
}

pessoa.descrever()