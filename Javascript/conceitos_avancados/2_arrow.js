//Tá criando um contexto novo e isolando o código
function funcao1(){
    console.log(this)
}

//Em arrow function, isso não acontece
const funcao2 = () => {
    console.log(this)
}

const mateus = {
    nome: 'Mateus',
    funcao1,
    funcao2
}

mateus.funcao1()
mateus.funcao2()