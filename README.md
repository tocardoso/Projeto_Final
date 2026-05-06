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
 
 
## Descrição do jogo

Este é uma adaptação em Python do clássico Jogo da Forca. O programa desafia o utilizador a adivinhar uma palavra, com introdução letra a letra, escolhida aleatoriamente de uma lista pré-determinada no programa. 
O projeto, no âmbito da UFCD de Programação em Python, foi desenhado de forma modular, separando a execução (`main.py`) da lógica (`jogo.py`) e dos dados (`palavras.txt`), incluindo tratamentos de erro (`try/except`) para garantir que o jogo seja suficientemente robusto contra falhas de leitura ou inputs inválidos.

## Principais Regras

O jogador tem um máximo de 6 tentativas falhadas.
Se a letra introduzida existir na palavra, o sistema revela a sua posição. Caso contrário, subtrai uma tentativa.
O sistema apenas aceita letras individuais (A-Z). Números, símbolos ou múltiplas letras são rejeitados sem penalização.
O jogador é avisado se tentar introduzir uma letra que já foi utilizada anteriormente.
O jogador ganha o jogo quando todas as letras da palavra são descobertas dentro das 6 tentativas permitidas.
O jogador perde o jogo quando esgota todas as 6 tentativas antes de completar a palavra.

## Instruções de Execução

1. Possuir o **Python 3.x** instalado.
2. Fazer o download ou clonar o repositório Projeto Final
3. Garantir que os ficheiros `main.py`, `jogo.py` e `palavras.txt` estão na mesma pasta.
4. Abrir o terminal ou a linha de comandos na pasta do projeto e executar o comando python main.py
5. (Opcional) Editar o ficheiro `palavras.txt` para adicionar ou remover palavras do jogo.

## Exemplo de Utilização

--- Jogo da Forca ---

Palavra: _ _ _ _ _ _ _ _ _ _
Digite uma letra: 

Palavra: _ _ _ _ _ _ _ _ _ _
Digite uma letra: G
Errado! Tentativas restantes: 5

alavra: _ _ _ _ _ _ A _ _ _
Digite uma letra: c

Palavra: C _ _ _ _ _ A _ _ _
Digite uma letra: 
...
Ganhaste! A palavra era: (palavrada escolhida aleatóriamente)

