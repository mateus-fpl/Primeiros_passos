function calcularJuros(c, i, t){
    M = c *(1+i)**t
    return M
}

let c = 100
let i = 0.05
let t = 10

let resultado = calcularJuros(c, i, t)
console.log ("O resultado do investimento será R$: " + resultado.toFixed(2))