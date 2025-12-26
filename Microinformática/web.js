//Exercício 1:
let nome = "Mateus"
let idade = 33
let almoco = true

console.log("EXERCICIO 1:")
console.log(typeof nome)
console.log(typeof idade)
console.log(typeof almoco)
console.log("\n")

//Exercício 2:
let num1 = 10
let num2 = 5
let soma = num1 + num2
let sub = num1 - num2
let mult = num1 * num2
let div = num1 / num2
console.log("EXERCICIO2:")
console.log ("num1 + num2 = " + soma + "\nnum1 - num2 = " + sub + "\nnum1 * num2 = " + mult + "\nnum1 / num2 = " + div + "\n")


//Exercício 3:
let city = "Osasco"
let state = "Sao Paulo"
console.log("EXERCICIO 3:")
console.log("Eu moro em " + city + " no estado de " + state) 
console.log(`Eu moro em ${city} no estado de ${state} \n`)

//Exercício 4:
let age = 14
let canDrive = 18
console.log("EXERCICIO 4:")
if (age >= 18){
    console.log("Você pode tirar sua CNH")
} else {
   let stop = canDrive - age
    console.log(`Faltam ${stop} anos para você poder tirar sua habilitação! \n`)
}

//Exercício 5:
let number = 7
console.log("EXERCICIO 5:")
for (let i = 0; i < 11; i++){
    let tabuada = i * number
    console.log(number + " * " + i + " = " + tabuada + "\n")
}

//Exercicio 6:
let num = 25
let nom = "25"
console.log("EXERCICIO 6:")
console.log(num == nom )
console.log(num === nom)
//Explicação do que aconteceu no console abaixo
console.log("A primeira variável é verdadeira porque consegue comparar o numero com o String. Ja a segunda e falsa porque tres sinais de iguais faz uma comparaçao muito mais especifica \n")

//Exercicio 7:
let day = 3
console.log("EXERCICIO 7:")
switch (day){
    case 1:
    console.log("Domingo")
    break
    case 2:
    console.log("Segunda-feira")
    break
    case 3:
    console.log("Terça-feira")
    break
    case 4:
    console.log("Quarta-feira")
    break
    case 5:
    console.log("Quinta-feira")
    break
    case 6:
    console.log("Sexta-feira")
    break
    case 7:
    console.log("Sábado")
    break
}
console.log("\n")

//Exercício 8:
let ten = 10
console.log("EXERCICIO 8:")
while (ten >= 5){
    console.log(ten)
    ten--
}


//Exercício 9:
console.log("EXERCICIO 9")
for (let i = 3; i <= 20; i++) {
  if (i % 2 !== 0) {
  continue
  }

  console.log("Encontrei um número par: " + i)
  
  break
}

console.log("\n")

//Exercício 10:
console.log("EXERCICIO 10:")
let nu1 = console.log("Digite o primeiro número:")
let nu2 = console.log("Digite o segundo número:")
let operacao = console.log("Digite a operação (+, -, *, /):")

nu1 = parseFloat(nu1)
nu2 = parseFloat(nu2)

let resultado

if (operacao === "+") {
  resultado = nu1 + nu2
  console.log("O resultado é: " + resultado)
} else if (operacao === "-") {
  resultado = nu1 - nu2
  console.log("O resultado é: " + resultado)
} else if (operacao === "*") {
  resultado = nu1 * nu2
  console.log("O resultado é: " + resultado)
} else if (operacao === "/") {
  // Adiciona um tratamento para a divisão por zero
  if (nu2 !== 0) {
    resultado = nu1 / nu2
    console.log("O resultado é: " + resultado)
  } else {
    console.log("Erro: Divisão por zero não é permitida.")
  }
} else {
  console.log("Operação inválida. Por favor, use +, -, * ou /.")
}
