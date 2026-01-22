# Missão Escape Room – Jogo Educativo em Python (CLI)
# Projeto exemplo completo que cumpre todos os requisitos

import random

# -----------------------------
# Estrutura do Jogador
# -----------------------------

def criar_jogador(nome):
    return {
        "nome": nome,
        "moedas": 20,
        "energia": 100,
        "inventario": [],
        "historico": [],
        "missoes": {
            "Primeiro Desafio": False,
            "Primeira Compra": False
        }
    }

# -----------------------------
# Menu Principal
# -----------------------------

def menu():
    print("\n=== MISSÃO ESCAPE ROOM ===")
    print("1. Jogar desafio")
    print("2. Loja")
    print("3. Ver estado do jogador")
    print("4. Ver missões")
    print("5. Relatório final")
    print("6. Sair")
    return input("Escolha uma opção: ")

# -----------------------------
# Desafios
# -----------------------------

def desafio_matematica(jogador):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    resposta = int(input(f"Quanto é {a} + {b}? "))

    if resposta == a + b:
        print("Resposta correta! +5 moedas")
        jogador["moedas"] += 5
        jogador["missoes"]["Primeiro Desafio"] = True
    else:
        print("Resposta errada! -3 moedas")
        jogador["moedas"] -= 3


def desafio_palavra(jogador):
    palavras = ["python", "escape", "codigo"]
    secreta = random.choice(palavras)
    tentativa = input("Adivinha a palavra secreta: ")

    if tentativa.lower() == secreta:
        print("Acertaste! +7 moedas")
        jogador["moedas"] += 7
        jogador["missoes"]["Primeiro Desafio"] = True
    else:
        print(f"Errado! A palavra era '{secreta}'. -2 moedas")
        jogador["moedas"] -= 2


def jogar_desafio(jogador):
    print("\nEscolhe um desafio:")
    print("1. Matemática")
    print("2. Palavra Secreta")
    escolha = input("Opção: ")

    if escolha == "1":
        desafio_matematica(jogador)
    elif escolha == "2":
        desafio_palavra(jogador)
    else:
        print("Opção inválida!")

# -----------------------------
# Loja
# -----------------------------

def loja(jogador):
    itens = {
        "Poção de Energia": 10,
        "Chave Misteriosa": 15
    }

    print("\n=== LOJA ===")
    for item, preco in itens.items():
        print(f"{item} - {preco} moedas")

    escolha = input("O que deseja comprar? (ou 'sair'): ")

    if escolha in itens:
        if jogador["moedas"] >= itens[escolha]:
            jogador["moedas"] -= itens[escolha]
            jogador["inventario"].append(escolha)
            jogador["missoes"]["Primeira Compra"] = True
            print(f"Compraste {escolha}!")
        else:
            print("Moedas insuficientes!")
    elif escolha.lower() == "sair":
        return
    else:
        print("Item inválido!")

# -----------------------------
# Estado do Jogador
# -----------------------------

def ver_estado(jogador):
    print("\n=== ESTADO DO JOGADOR ===")
    print(f"Nome: {jogador['nome']}")
    print(f"Moedas: {jogador['moedas']}")
    print(f"Energia: {jogador['energia']}")
    print(f"Inventário: {jogador['inventario']}")

# -----------------------------
# Missões
# -----------------------------

def ver_missoes(jogador):
    print("\n=== MISSÕES ===")
    for missao, concluida in jogador["missoes"].items():
        estado = "Concluída" if concluida else "Pendente"
        print(f"{missao}: {estado}")

# -----------------------------
# Relatório Final
# -----------------------------

def relatorio_final(jogador):
    print("\n=== RELATÓRIO FINAL ===")
    print(f"Jogador: {jogador['nome']}")
    print(f"Moedas finais: {jogador['moedas']}")
    print(f"Itens adquiridos: {jogador['inventario']}")
    print("Missões concluídas:")
    for m, c in jogador["missoes"].items():
        if c:
            print(f"- {m}")

# -----------------------------
# Programa Principal
# -----------------------------

nome = input("Digite o nome do jogador: ")
jogador = criar_jogador(nome)

while True:
    opcao = menu()

    if opcao == "1":
        jogar_desafio(jogador)
    elif opcao == "2":
        loja(jogador)
    elif opcao == "3":
        ver_estado(jogador)
    elif opcao == "4":
        ver_missoes(jogador)
    elif opcao == "5":
        relatorio_final(jogador)
    elif opcao == "6":
        print("Obrigado por jogar!")
        break
    else:
        print("Opção inválida!")