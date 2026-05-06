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
 
