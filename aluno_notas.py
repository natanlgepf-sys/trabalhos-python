import os

# ----------------- DADOS -----------------
alunos = []
contador_codigo = 1


# ----------------- FUNÇÕES AUXILIARES -----------------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def gerar_codigo():
    global contador_codigo
    codigo = f"{contador_codigo:04d}"
    contador_codigo += 1
    return codigo


def input_ou_voltar(mensagem):
    valor = input(mensagem)
    if valor.lower() == "v":
        return None
    return valor


# ----------------- CADASTRO -----------------
def cadastrar_aluno():
    limpar_tela()
    print("=== Cadastrar Aluno ===")
    print("Digite 'v' a qualquer momento para voltar\n")

    nome = input_ou_voltar("Nome do aluno: ")
    if nome is None:
        return

    notas = []
    for i in range(3):
        while True:
            entrada = input_ou_voltar(
                f"Nota {i + 1} (0 a 20, máx. 2 casas decimais): "
            )
            if entrada is None:
                return

            try:
                # valida casas decimais
                if "." in entrada:
                    if len(entrada.split(".")[1]) > 2:
                        print("A nota deve ter no máximo 2 casas decimais.")
                        continue

                nota = float(entrada)

                if 0 <= nota <= 20:
                    notas.append(round(nota, 2))
                    break
                else:
                    print("A nota deve estar entre 0 e 20.")
            except ValueError:
                print("Digite um número válido.")

    aluno = {
        "codigo": gerar_codigo(),
        "nome": nome,
        "notas": notas
    }

    alunos.append(aluno)
    print(f"\nAluno cadastrado com sucesso!")
    print(f"Código do aluno: {aluno['codigo']}")
    input("\nPressione ENTER para continuar...")


# ----------------- LISTAR -----------------
def listar_alunos():
    limpar_tela()
    print("=== Lista de Alunos ===\n")

    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            print(f"Código: {aluno['codigo']}")
            print(f"Nome: {aluno['nome']}")
            print(f"Notas: {[f'{n:.2f}' for n in aluno['notas']]}")
            print(f"Média: {media:.2f}")
            print("-" * 30)

    input("\nPressione ENTER ou 'v' para voltar...")


# ----------------- MÉDIAS -----------------
def mostrar_medias():
    limpar_tela()
    print("=== Médias ===\n")

    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        soma = 0
        for aluno in alunos:
            media = sum(aluno["notas"]) / len(aluno["notas"])
            soma += media
            print(f"{aluno['codigo']} - {aluno['nome']} | Média: {media:.2f}")

        print(f"\nMédia geral da turma: {(soma / len(alunos)):.2f}")

    input("\nPressione ENTER ou 'v' para voltar...")


# ----------------- ELIMINAR -----------------
def eliminar_aluno():
    limpar_tela()
    print("=== Eliminar Aluno ===\n")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        input("\nPressione ENTER para voltar...")
        return

    print("Alunos cadastrados:")
    for aluno in alunos:
        print(f"{aluno['codigo']} - {aluno['nome']}")

    codigo = input_ou_voltar("\nDigite o código do aluno a eliminar: ")
    if codigo is None:
        return

    for aluno in alunos:
        if aluno["codigo"] == codigo:
            alunos.remove(aluno)
            print("\nAluno eliminado com sucesso!")
            input("\nPressione ENTER para continuar...")
            return

    print("\nCódigo não encontrado.")
    input("\nPressione ENTER para continuar...")


# ----------------- MENU -----------------
def menu():
    limpar_tela()
    print("=== Sistema Escolar ===")
    print("1. Cadastrar aluno")
    print("2. Listar alunos e notas")
    print("3. Mostrar médias")
    print("4. Eliminar aluno")
    print("5. Sair")


# ----------------- PROGRAMA PRINCIPAL -----------------
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        mostrar_medias()
    elif opcao == "4":
        eliminar_aluno()
    elif opcao == "5":
        limpar_tela()
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")
        input("\nPressione ENTER para continuar...")
