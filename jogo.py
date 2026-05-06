# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:25:19 2026

@author: Secretaria
"""

import random
import os

def carregar_palavras():
    # Garante que o Python encontra o ficheiro na mesma pasta do script
    diretorio = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(diretorio, "palavras.txt")
    
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return [linha.strip().upper() for linha in f if linha.strip()]
    except FileNotFoundError:
        # Caso o ficheiro não exista, usa uma lista de segurança
        return ["PYTHON", "ALGORITMO"]

def jogar_forca():
    palavras = carregar_palavras()
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    tentativas_restantes = 6
    letras_tentadas = []

    print("--- Bem-vindo ao Jogo da Forca! ---")

    while tentativas_restantes > 0 and "_" in letras_descobertas:
        print(f"\nPalavra: {' '.join(letras_descobertas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras tentadas: {', '.join(letras_tentadas)}")

        palpite = input("Digite uma letra: ").upper().strip()

        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, introduz apenas uma letra válida.")
            continue

        if palpite in letras_tentadas:
            print(f"A letra '{palpite}' já foi usada. Tenta outra!")
            continue

        letras_tentadas.append(palpite)

        if palpite in palavra_secreta:
            print(f"Boa! A letra '{palpite}' existe na palavra.")
            for i, letra in enumerate(palavra_secreta):
                if letra == palpite:
                    letras_descobertas[i] = palpite
        else:
            print(f"Errado! A letra '{palpite}' não existe.")
            tentativas_restantes -= 1

    if "_" not in letras_descobertas:
        print(f"\nPARABÉNS! Ganhaste! A palavra era: {palavra_secreta}")
    else:
        print(f"\nGAME OVER! Esgotaste as tentativas. A palavra era: {palavra_secreta}")

def carregar_palavras():
    try:
        with open("palavras.txt", "r") as f:
            return [l.strip().upper() for l in f if l.strip()]
    except:
        return ["PADRAO"]

def desenhar_forca(erros):
    estados = [
        "  +---+\n      |\n      |\n      |",
        "  +---+\n  O   |\n      |\n      |",
        "  +---+\n  O   |\n  |   |\n      |",
        "  +---+\n  O   |\n /|   |\n      |",
        "  +---+\n  O   |\n /|\\  |\n      |",
        "  +---+\n  O   |\n /|\\  |\n /    |",
        "  +---+\n  O   |\n /|\\  |\n / \\  |"
    ]
    return estados[erros]

def iniciar_partida():
    palavra = random.choice(carregar_palavras())
    tabuleiro = ["_" for _ in palavra]
    erros = 0
    usadas = []

    while erros < 6 and "_" in tabuleiro:
        print(desenhar_forca(erros))
        print(f"\nPalavra: {' '.join(tabuleiro)}")
        print(f"Letras usadas: {usadas}")
        
        letra = input("Letra: ").upper()
        if letra in usadas or len(letra) != 1: continue
        
        usadas.append(letra)
        if letra in palavra:
            for i, l in enumerate(palavra):
                if l == letra: tabuleiro[i] = letra
        else:
            erros += 1

    print("\nVitória!" if "_" not in tabuleiro else f"\nDerrota! Era: {palavra}")
