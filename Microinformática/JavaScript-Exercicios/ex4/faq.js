// 1. Referências aos elementos HTML
const perguntaElemento = document.getElementById('pergunta1');
const respostaElemento = document.getElementById('resposta1');

// 2. Função para alternar a visibilidade da resposta
function alternarVisibilidade() {
    // classList.toggle('escondido') faz o seguinte:
    // 1. Se a classe 'escondido' estiver presente, ela é removida (mostra a resposta).
    // 2. Se a classe 'escondido' NÃO estiver presente, ela é adicionada (esconde a resposta).
    respostaElemento.classList.toggle('escondido');
}

// 3. Associar a função ao evento de clique na pergunta
perguntaElemento.addEventListener('click', alternarVisibilidade);

console.log("FAQ Interativo pronto!");