function calcularIMC(peso, altura) {
    return peso / Math.pow(altura, 2)
}

function classificarIMC(imc) {
    if (imc < 18.5) {
        return 'Abaixo do peso';
    } else if (imc < 24.9) {
        return 'Peso ideal.';
    } else if (imc < 29.9) {
        return 'Levemente acima do peso';
    } else if (imc < 34.9) {
       return 'Obesidade Grau I';
    } else if (imc < 39.9) {
        return 'Obesidade Grau II (severa)';
    } else {
        return 'Obesidade Grau III (mórbida)';
    }
}

function main(){
const peso = 88
const alt = 1.85
const imc = calcularIMC(peso, alt)
console.log(classificarIMC(imc))
}

main()

