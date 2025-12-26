function calcularCirculo(raio) {
    area = Math.PI * (raio ** 2)
    peri = 2 * Math.PI * raio
    return {area: area,
            peri: peri
    }
}
let raio = 5
const resultados = calcularCirculo(raio)
let r_area = resultados.area.toFixed(2)
let r_peri = resultados.peri.toFixed(2)

console.log("A área do círculo é " + r_area + " e o perímetro é " + r_peri)
