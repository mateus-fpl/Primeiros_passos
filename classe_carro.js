class carro{
    marca
    cor 
    gastoMedioPorKm

    constructor(marca,cor,gastoMedioPorKm){
        this.marca = marca
        this.cor = cor
        this.gastoMedioPorKm = gastoMedioPorKm
    }

    calcularGastodePercurso(distanciaEmKm, precoDeCombustivel){
        return distanciaEmKm * this.gastoMedioPorKm * precoDeCombustivel
    }
}
const uno = new carro("FIAT","vermelho",1/12)
console.log("O gasto para 70 Km é: R$ " + uno.calcularGastodePercurso(70,5).toFixed(2))

const camaro = new carro("chevrolet","amarelo",1/5)
console.log("O gasto para 70 Km é: R$ " + camaro.calcularGastodePercurso(70,5).toFixed(2))

