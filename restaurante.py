import os

# ================== DADOS ==================
restaurantes = []


# ================== FUNÇÕES AUXILIARES ==================
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def input_ou_voltar(mensagem):
    valor = input(mensagem)
    if valor.lower() == "v":
        return None
    return valor


def estado_texto(estado):
    return "Ativado" if estado else "Desativado"


# ================== CADASTRAR RESTAURANTE ==================
def cadastrar_restaurante():
    limpar_tela()
    print("=== Cadastrar Restaurante ===")
    print("Digite 'v' a qualquer momento para voltar\n")

    nome = input_ou_voltar("Nome do restaurante: ")
    if nome is None:
        return

    categoria = input_ou_voltar("Categoria: ")
    if categoria is None:
        return

    restaurante = {
        "nome": nome,
        "categoria": categoria,
        "ativo": False
    }

    restaurantes.append(restaurante)

    print("\nRestaurante cadastrado com sucesso!")
    print("Estado inicial: Desativado")
    input("\nPressione ENTER para continuar...")


# ================== LISTAR RESTAURANTES ==================
def listar_restaurantes():
    limpar_tela()
    print("=== Lista de Restaurantes ===\n")

    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
    else:
        for r in restaurantes:
            print(f"Nome: {r['nome']}")
            print(f"Categoria: {r['categoria']}")
            print(f"Estado: {estado_texto(r['ativo'])}")
            print("-" * 30)

    input("\nPressione ENTER ou 'v' para voltar...")


# ================== ATIVAR / DESATIVAR ==================
def alterar_estado():
    limpar_tela()
    print("=== Ativar / Desativar Restaurante ===")
    print("Digite 'v' para voltar\n")

    if not restaurantes:
        print("Nenhum restaurante cadastrado.")
        input("\nPressione ENTER para voltar...")
        return

    print("Restaurantes cadastrados:\n")
    for r in restaurantes:
        print(f"Nome: {r['nome']} | Estado: {estado_texto(r['ativo'])}")

    nome = input_ou_voltar("\nDigite o nome do restaurante: ")
    if nome is None:
        return

    for r in restaurantes:
        if r["nome"].lower() == nome.lower():
            r["ativo"] = not r["ativo"]
            print("\nEstado alterado com sucesso!")
            print(f"Novo estado: {estado_texto(r['ativo'])}")
            input("\nPressione ENTER para continuar...")
            return

    print("\nRestaurante não encontrado.")
    input("\nPressione ENTER para continuar...")


# ================== MENU ==================
def menu():
    limpar_tela()
    print("=== Gestão de Restaurantes ===")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurantes")
    print("3 - Ativar/Desativar restaurante")
    print("4 - Sair")


# ================== PROGRAMA PRINCIPAL ==================
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_restaurante()
    elif opcao == "2":
        listar_restaurantes()
    elif opcao == "3":
        alterar_estado()
    elif opcao == "4":
        limpar_tela()
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
        input("\nPressione ENTER para continuar...")
