
function sayMyName(name){
    console.log('Your name is ' + name)
}

sayMyName("Mateus")
sayMyName("Amanda")

function quadrado(valor){
    return valor*valor
}
const quadradoDeDez = quadrado(10)
console.log (quadrado(10) + quadrado(10))

function incrementarJuros(valor, percentualJuros){
    const valorDeAcrescimo = (percentualJuros/100) * valor
    return valor + valorDeAcrescimo
}
console.log(incrementarJuros(100,10))
console.log(incrementarJuros(100,15))



