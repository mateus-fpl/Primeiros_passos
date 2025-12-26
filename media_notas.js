let nota1 = 8
let nota2 = 5
let nota3 = 7
let nota4 = 6.5
let nota5 = 5.5

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5
 
if (media < 5){
    console.log("Reprovado!")
} else if (media < 7){
    console.log("Recuperação.")
} else {
    console.log("Aprovado")
}

const notas = []
notas.push(8)
notas.push(5)
notas.push(7)
notas.push(6.5)
notas.push(5.5)

const soma = notas[0] + notas[1] + notas[2] + notas[3] + notas[4]

med = (soma/notas.length)

if (med < 5){
    console.log("Reprovado!")
} else if (med < 7){
    console.log("Recuperação.")
} else {
    console.log("Aprovado")
}