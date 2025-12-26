// 1. Referências aos elementos HTML
const tarefaInput = document.getElementById('tarefa-input');
const btnAdicionar = document.getElementById('btn-adicionar');
const listaTarefas = document.getElementById('lista-de-tarefas');

// 2. Função principal para adicionar a tarefa
function adicionarTarefa() {
    // Pega o texto do input e remove espaços em branco extras
    const textoTarefa = tarefaInput.value.trim();

    // Validação: Só adiciona se o campo não estiver vazio
    if (textoTarefa === "") {
        alert("Por favor, digite uma tarefa válida.");
        return; // Sai da função se estiver vazio
    }

    // A - Cria um novo elemento <li>
    const novoItem = document.createElement('li');

    // B - Define o conteúdo do novo <li>
    novoItem.textContent = textoTarefa;

    // C - Adiciona o novo <li> ao <ul>
    listaTarefas.appendChild(novoItem);

    // D - Limpa o campo de input (Opcional)
    tarefaInput.value = "";
    
    // Opcional: Coloca o foco de volta no input para que o usuário digite a próxima rapidamente
    tarefaInput.focus();
}

// 3. Associar a função ao evento de clique do botão
btnAdicionar.addEventListener('click', adicionarTarefa);

// Opcional: Permitir que o usuário adicione a tarefa apertando ENTER
tarefaInput.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        adicionarTarefa();
    }
});