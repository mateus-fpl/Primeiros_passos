# ⏳ Exercício 10: O Jogo da Forca com Relógio Regressivo (Nível Arquiteto de Software)
# Cenário: Um jogo de adivinhação onde o tempo é o seu pior inimigo. O jogador tem uma palavra secreta para adivinhar, mas a cada tentativa (ou a cada rodada), o sistema valida quanto tempo exato falta para um limite estourar (ou um cronômetro regressivo baseado nos segundos atuais do minuto).

# O que fazer:

# Defina uma palavra secreta (ex: "python").

# Crie uma mecânica de loop onde o usuário tenta adivinhar uma letra.

# O grande desafio temporal: A cada interação (ou a cada loop), capture o segundo atual usando o datetime.now().second.

# Implemente uma regra de "bomba-relógio": por exemplo, o usuário tem um limite onde os segundos correm contra ele (ex: se o segundo atual for múltiplo de algo, ou criar um timer regressivo real de 30 segundos usando a diferença de datetime.now()). Se o tempo esgotar antes de acertar a palavra, imprima "⏰ O tempo acabou! Você perdeu!".

# Caso acerte todas as letras antes do tempo, imprima "🎉 Parabéns, você venceu a tempo!".