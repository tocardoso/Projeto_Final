# Jogo da Forca - Projeto Final

## Definição do problema

 •	Criar uma versão do Jogo da Forca em programação Python para um utilizador jogar em ambiente de terminal (consola) do Windows ou ainda em IDEs ou Editores de Código Python.

## Objetivo do jogo

•	O objetivo é permitir que um utilizador descubra uma palavra secreta (armazenada ou selecionada aleatoriamente) letra por letra, uma de cada vez, preenchendo todos os espaços/traços vazios antes de esgotar o número máximo de tentativas permitidas.

## Regras principais

•	O programa seleciona aleatóriamente uma palavra da lista definida no código para cada jogo.
•	Apresenta a palavra sob a forma de traços, i.e, mostrando apenas tracinhos (_) no lugar de cada letra da palavra escolhida.
•	O utilizador introduz uma letra de cada vez:
    Se a letra sugerida existir na palavra, o sistema revela a sua posição (ou posições).
    Se a letra não existir, o sistema contabiliza um erro e reduz o número de tentativas restantes.
•	O sistema deve manter um registo das letras já utilizadas para evitar repetições inúteis.

## Condições de vitória/derrota
•	Vitória: O jogador ganha se conseguir preencher todas as lacunas (_) da palavra secreta.
•	Derrota: O jogador perde se cometer o número máximo de erros permitido antes de completar a palavra. Quando ele perde, (esgota o número máximo de tentativas) o jogo revela qual era a palavra correta.

## Limitações do jogo
•	Número de tentativas definido  - 6.
•	Deve aceitar apenas caracteres alfabéticos (A-Z). Se o utilizador digitar um número, um símbolo ou deixar em branco, o jogo deve avisar que a entrada é inválida.
•	O sistema deve ser insensível a maiúsculas/minúsculas (case-insensitive).
•	Deve validar entradas inválidas (números, símbolos ou múltiplas letras de uma vez).
•	O jogo deve operar sobre um conjunto pré-definido de palavras (strings) de comprimento variável.
•	jogo será executado em modo consola, sem interface gráfica.

## Requisitos Funcionais (RF) - Estes descrevem as funcionalidades diretas e as ações do utilizador
1.	RF01 - Seleção Aleatória de Palavras: O sistema deve selecionar aleatoriamente uma palavra de um banco de dados ou lista pré-definida no início de cada partida.
2.	RF02 - Validação da Entrada: O sistema deve aceitar apenas caracteres alfabéticos, impedindo o uso de números ou símbolos e tratando letras maiúsculas e minúsculas como iguais.
3.	RF03 - Atualização do Estado da Palavra: Sempre que o jogador acertar uma letra, o sistema deve revelar a posição exata dessa letra na palavra escondida.
4.	RF04 - Controlar Tentativas e Erros: O sistema deve contabilizar os erros e diminuir o número de tentativas restantes (limite de 6) sempre que uma letra incorreta for inserida.
5.	RF05 - Histórico de Letras: O sistema deve armazenar e exibir na tela todas as letras que já foram digitadas pelo jogador para evitar repetições.
6.	RF06 - Notificação do Resultado: O sistema deve emitir uma mensagem clara de "Vitória" ou "Derrota" assim que uma das condições de encerramento for atingida.

## Requisitos Não Funcionais (NRF) - Estes descrevem as qualidades do sistema, como desempenho, usabilidade e segurança.
1.	RNF01 - Usabilidade (Simplicidade): A interface deve ser textual, intuitiva e fornecer feedback imediato ao utilizador após cada jogada (ex: avisar se a letra é repetida).
2.	RNF02 - Portabilidade (Linguagem): O jogo deve ser executável em qualquer sistema operativo que possua o interpretador Python 3.x instalado.
3.	RNF03 - Desempenho: O sistema deve processar cada jogada e atualizar a tela em menos de 1 segundo, garantindo que o jogo não pareça "travado".


