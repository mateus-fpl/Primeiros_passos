# ### 🤺 Desafio: Colisão de Arenas Pokémon

# Imagine um jogo onde duas arenas $3 \times 3$ se cruzam no campo de batalha:

# * **Matriz 1 (Arena 1):** Guarda os **nomes/espécies** dos Pokémon em cada coordenada.
# * **Matriz 2 (Arena 2):** Guarda o **nível (Level/Power)** dos Pokémon nas mesmas coordenadas exactas.

# #### O que você deve construir:

# 1. **Estrutura de Matrizes ($3 \times 3$):**
# * Monte a **Matriz 1** com 9 Pokémon de sua escolha (ex: `[0][0]` é o Pikachu, `[0][1]` é o Charizard, etc.).
# * Monte a **Matriz 2** com os níveis de cada um (números de 1 a 100) exatamente nas mesmas posições.


# 2. **Classes (POO com Polimorfismo):**
# * **Classe Pai `Pokemon`:**
# * Atributos: `nome` e `nivel`.
# * Método `atacar()`: Exibe algo genérico como `"Pokémon X (Nível Y) lança um ataque básico!"`.


# * **Classe Filha `Eletrico` (Herda de `Pokemon`):**
# * Sobrescreva `atacar()`: `"Pokémon X (Nível Y) solta um Choque do Trovão!"`.


# * **Classe Filha `Fogo` (Herda de `Pokemon`):**
# * Sobrescreva `atacar()`: `"Pokémon X (Nível Y) lança uma Lança-Chamas!"`.




# 3. **A Mecânica de Cruzar as Matrizes:**
# * Faça um `for` duplo (`i` para linha, `j` para coluna) para varrer as duas matrizes **ao mesmo tempo**.
# * Em cada célula `[i][j]`, pegue o nome da Matriz 1 e o nível da Matriz 2.
# * Instancie a classe correspondente ao tipo dele (se for elétrico, crie um `Eletrico`, se for fogo, crie um `Fogo`).
# * Adicione esse objeto instanciado em uma **lista de combate**.


# 4. **O Duelo (O Grand Finale):**
# * Faça um `for` que percorre essa lista de combate fazendo os Pokémon duelarem em duplas (o índice 0 contra o índice 1, o 2 contra o 3, etc.) usando o método `.atacar()` de cada um!