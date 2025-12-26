let celsius = 40

function convertaCelsius(celsius){
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit
}

let resultado = convertaCelsius(celsius)

console.log ("O resultado é " + resultado.toFixed(2))