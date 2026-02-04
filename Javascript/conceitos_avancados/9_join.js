const lista = [{nome: 'Mateus'},{nome: 'Amanda'},{nome: 'Fuefa'}, {nome: 'Adailton'}]

console.log(lista.map(e => e.nome).filter((e) => e.startsWith('A'))
.join('; '))


