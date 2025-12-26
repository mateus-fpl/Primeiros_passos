// 1. Referências aos elementos HTML
const nomeInput = document.getElementById('nome-input');
const btnSaudar = document.getElementById('btn-saudar');
const mensagemParagrafo = document.getElementById('mensagem-saudacao');

// 2. Função principal que executa a saudação
function saudarUsuario() {
    // Pega o valor digitado no campo de texto
    const nome = nomeInput.value.trim(); // .trim() remove espaços em branco extras

    // Estrutura if/else para validação
    if (nome === "") {
        // Se o campo estiver vazio (condição 'if')
        mensagemParagrafo.textContent = "Por favor, digite seu nome.";
        mensagemParagrafo.style.color = "red"; // (Opcional) Deixa a mensagem de erro em vermelho
    } else {
        // Se o campo tiver um nome (condição 'else')
        mensagemParagrafo.textContent = `Olá, ${nome}! Seja bem-vindo(a)!`;
        mensagemParagrafo.style.color = "green"; // (Opcional) Deixa a mensagem de sucesso em verde
    }
}

// 3. Associar a função ao evento de clique do botão
btnSaudar.addEventListener('click', saudarUsuario);