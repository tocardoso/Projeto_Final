# -*- coding: utf-8 -*-
import random

def carregar_palavras():
    try:
        with open("palavras.txt", "r", encoding="utf-8") as f:
            return [linha.strip().upper() for linha in f if linha.strip()]
    except:
        # Se o ficheiro não existir ou der erro, usa esta lista padrão
        return ["PYTHON", "ALGORITMO", "LOGICA"]

def jogar_forca():
    palavras = carregar_palavras()
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    tentativas = 6
    letras_tentadas = []

    print("--- Jogo da Forca ---")

    while tentativas > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        
        try:
            palpite = input("Digite uma letra: ").upper().strip()
        except EOFError: 
            break # Sai do jogo se o terminal for fechado

        # Validações simples
        if len(palpite) != 1 or not palpite.isalpha():
            print("Entrada inválida!")
            continue

        if palpite in letras_tentadas:
            print("Já usaste esta letra!")
            continue

        letras_tentadas.append(palpite)

        if palpite in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[i] = palpite
        else:
            tentativas -= 1
            print(f"Errado! Tentativas restantes: {tentativas}")
            
            
    if "_" not in letras_descobertas:
        print(f"Ganhaste! A palavra era: {palavra_secreta}")
    else:
        print(f"Perdeste! A palavra era: {palavra_secreta}")
