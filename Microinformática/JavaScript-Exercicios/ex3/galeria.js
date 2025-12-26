// 1. Array com os links das imagens
// (Você pode substituir por links de imagens reais)
const imagens = [
    "https://picsum.photos/id/10/600/400",  // Imagem 1
    "https://picsum.photos/id/20/600/400",  // Imagem 2
    "https://picsum.photos/id/30/600/400",  // Imagem 3
    "https://picsum.photos/id/40/600/400"   // Imagem 4
];

// Variável para rastrear a posição atual no array (começa no índice 0)
let indiceAtual = 0;

// 2. Referências aos elementos HTML
const imagemElemento = document.getElementById('imagem-galeria');
const btnAnterior = document.getElementById('btn-anterior');
const btnProximo = document.getElementById('btn-proximo');
const statusParagrafo = document.getElementById('status-imagem');

// 3. Função para exibir a imagem atual e atualizar o status
function exibirImagemAtual() {
    // Pega a URL do array usando o índice atual
    imagemElemento.src = imagens[indiceAtual];
    
    // Atualiza o texto de status (ex: "Imagem 1 de 4")
    statusParagrafo.textContent = `Imagem ${indiceAtual + 1} de ${imagens.length}`;
}

// 4. Função para avançar (Próximo)
function avancarImagem() {
    // Verifica se o índice atual é menor que o último índice do array (array.length - 1)
    if (indiceAtual < imagens.length - 1) {
        indiceAtual++; // Avança para a próxima imagem
    } else {
        // Opcional: Volta para a primeira imagem (loop)
        indiceAtual = 0;
    }
    exibirImagemAtual();
}

// 5. Função para retroceder (Anterior)
function voltarImagem() {
    // Verifica se o índice atual é maior que 0 (a primeira imagem)
    if (indiceAtual > 0) {
        indiceAtual--; // Volta para a imagem anterior
    } else {
        // Opcional: Vai para a última imagem (loop)
        indiceAtual = imagens.length - 1; 
    }
    exibirImagemAtual();
}

// 6. Associar as funções aos cliques
btnProximo.addEventListener('click', avancarImagem);
btnAnterior.addEventListener('click', voltarImagem);

// Exibe a primeira imagem assim que o script carrega
exibirImagemAtual();