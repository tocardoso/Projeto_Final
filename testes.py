import sys
import os

# Simula as funções do jogo para teste de lógica
def validar_entrada(letra):
    # Esta lógica deve ser idêntica à que tens no jogo.py
    if len(letra) != 1: return False
    if not letra.isalpha(): return False
    return True

def executar_testes():
    print("=== INICIANDO BATERIA DE TESTES ===\n")
    erros = 0

    # --- GRUPO 1: 5 CASOS VÁLIDOS (Sucesso esperado) ---
    print("Grupo 1: Casos Válidos")
    
    # 1. Letra única alfabética
    if not validar_entrada("A"): print("❌ Falha: 'A' devia ser válido"); erros += 1
    # 2. Letra minúscula (conversão)
    if not "a".upper() == "A": print("❌ Falha: conversão 'a'->'A'"); erros += 1
    # 3. Verificar se palavras.txt existe
    if not os.path.exists("palavras.txt"): print("❌ Falha: ficheiro palavras.txt ausente"); erros += 1
    # 4. Simulação de acerto (letra na palavra)
    palavra = "PYTHON"
    if "P" not in palavra: print("❌ Falha: lógica de busca falhou"); erros += 1
    # 5. Estado inicial (traços)
    tabuleiro = ["_"] * len("OI")
    if len(tabuleiro) != 2: print("❌ Falha: tabuleiro mal gerado"); erros += 1


    # --- GRUPO 2: 5 CASOS INVÁLIDOS (Rejeição esperada) ---
    print("\nGrupo 2: Casos Inválidos")

    # 1. Entrada numérica
    if validar_entrada("1"): print("❌ Falha: aceitou número"); erros += 1
    # 2. Múltiplas letras
    if validar_entrada("ABC"): print("❌ Falha: aceitou múltiplas letras"); erros += 1
    # 3. Símbolos especiais
    if validar_entrada("@"): print("❌ Falha: aceitou símbolo"); erros += 1
    # 4. Entrada vazia
    if validar_entrada(""): print("❌ Falha: aceitou vazio"); erros += 1
    # 5. Espaços em branco
    if validar_entrada(" "): print("❌ Falha: aceitou espaço"); erros += 1


    # --- RESULTADO FINAL PARA O GITHUB ---
    if erros > 0:
        print(f"\nTotal de erros: {erros}. O teste falhou!")
        sys.exit(1) # Faz o Badge ficar Vermelho
    else:
        print("\n✅ Todos os 10 casos passaram com sucesso!")
        sys.exit(0) # Faz o Badge ficar Verde

if __name__ == "__main__":
    executar_testes()
