class pessoa {
    pessoa
    peso
    altura

    constructor(pessoa, peso, altura) {
        this.pessoa = pessoa
        this.peso = peso
        this.altura = altura
    }

    calcularIMC() {
        return this.peso / Math.pow(this.altura, 2)

    }

    classificarIMC() {
        const imc = this.calcularIMC()

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
}

const pessoa1 = new pessoa("Mateus", 88.5, 1.85)
console.log("O(a) " + pessoa1.pessoa + " pesa " + pessoa1.peso + " e tem " + pessoa1.altura +
    " de altura. Seu IMC é: " + pessoa1.calcularIMC().toFixed(2))
    console.log(pessoa1.classificarIMC())