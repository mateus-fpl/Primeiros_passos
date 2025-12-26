// 1. Variável para guardar o valor atual do contador
let contador = 0;

// 2. Referências aos elementos HTML
const valorDisplay = document.getElementById('contador-valor');
const btnIncrementar = document.getElementById('btn-incrementar');
const btnResetar = document.getElementById('btn-resetar');

// Função auxiliar para atualizar o texto na tela
function atualizarDisplay() {
    valorDisplay.textContent = contador;
}

// 3. Função para Incrementar
function incrementar() {
    contador = contador + 1; // ou contador++;
    atualizarDisplay();
}

// 4. Função para Resetar
function resetar() {
    contador = 0;
    atualizarDisplay();
}

// 5. Associar as funções aos eventos de clique dos botões
btnIncrementar.addEventListener('click', incrementar);
btnResetar.addEventListener('click', resetar);