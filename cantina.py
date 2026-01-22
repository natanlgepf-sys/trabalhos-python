import os
from datetime import datetime

# ---------------- FUNÇÕES DE TELA ----------------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa(msg="\nPressione ENTER para continuar..."):
    input(msg)

# ---------------- DADOS ----------------
alunos = []
reservas = []

# Listas fixas de pratos, bebidas e sobremesas
ementa = {
    1: {"nome": "Bife com arroz", "preco": 5.00},
    2: {"nome": "Frango assado", "preco": 4.50},
    3: {"nome": "Massa vegetariana", "preco": 4.00}
}

bebidas = {
    1: {"nome": "Água", "preco": 1.00},
    2: {"nome": "Sumo", "preco": 1.50}
}

sobremesas = {
    1: {"nome": "Maçã", "preco": 0.80},
    2: {"nome": "Banana", "preco": 0.70},
    3: {"nome": "Salada de frutas", "preco": 1.50},
    4: {"nome": "Iogurte natural", "preco": 1.00}
}

# ---------------- FUNÇÕES AUXILIARES ----------------
def listar_alunos_com_codigo():
    if not alunos:
        print("⚠️ Nenhum aluno cadastrado.")
        return
    print(f"{'Código':<6} {'Nome':<10}")
    print("-"*20)
    for a in alunos:
        print(f"{a['codigo']:<6} {a['nome']:<10}")

def encontrar_aluno(codigo):
    for a in alunos:
        if a["codigo"] == codigo:
            return a
    return None

def mostrar_ementa():
    print("\n--- PRATOS ---")
    for k, v in ementa.items():
        print(f"{k} - {v['nome']} (€{v['preco']:.2f})")
    print("\n--- BEBIDAS ---")
    for k, v in bebidas.items():
        print(f"{k} - {v['nome']} (€{v['preco']:.2f})")
    print("\n--- SOBREMESAS ---")
    for k, v in sobremesas.items():
        print(f"{k} - {v['nome']} (€{v['preco']:.2f})")

def input_ou_voltar(texto):
    valor = input(f"{texto} (ou 'V' para voltar): ").strip()
    if valor.upper() == "V":
        return None
    if valor == "":
        return None
    return valor

# ---------------- FUNCIONALIDADES ----------------
def cadastrar_aluno():
    limpar_tela()
    print("📄 Página: Cadastrar Aluno\n")
    
    while True:
        nome = input_ou_voltar("Nome do aluno (máx 10 caracteres)")
        if nome is None: return
        if len(nome) == 0 or len(nome) > 10:
            print("❌ Nome inválido! Máximo 10 caracteres.")
        else:
            break

    while True:
        codigo = input_ou_voltar("Código do aluno (0 a 9999)")
        if codigo is None: return
        if not codigo.isdigit():
            print("❌ Código inválido!")
            continue
        codigo = int(codigo)
        if not (0 <= codigo <= 9999):
            print("❌ Código fora do intervalo!")
            continue
        if encontrar_aluno(codigo):
            print("❌ Código já existe!")
            continue
        break

    alunos.append({"nome": nome, "codigo": codigo})
    print(f"\n✅ Aluno cadastrado com sucesso! Código: {codigo}")
    pausa()

def listar_alunos():
    limpar_tela()
    print("📄 Página: Lista de Alunos\n")
    listar_alunos_com_codigo()
    pausa()

def fazer_reserva():
    limpar_tela()
    print("📄 Página: Fazer Reserva\n")
    if not alunos:
        print("⚠️ Nenhum aluno cadastrado.")
        pausa()
        return
    listar_alunos_com_codigo()
    cod = input_ou_voltar("Código do aluno")
    if cod is None or not cod.isdigit() or not encontrar_aluno(int(cod)):
        print("❌ Aluno não encontrado!")
        pausa()
        return
    cod = int(cod)

    while True:
        data = input_ou_voltar("Data da reserva (YYYY-MM-DD, ex: 2026-03-23)")
        if data is None: return
        try:
            datetime.strptime(data, "%Y-%m-%d")
            break
        except ValueError:
            print("❌ Formato inválido! Use YYYY-MM-DD com hífens, ex: 2026-03-23")

    mostrar_ementa()
    try:
        prato = input_ou_voltar("Escolha o prato (número)")
        if prato is None: return
        bebida = input_ou_voltar("Escolha a bebida (número)")
        if bebida is None: return
        sobremesa = input_ou_voltar("Escolha a sobremesa (número)")
        if sobremesa is None: return
        prato = int(prato)
        bebida = int(bebida)
        sobremesa = int(sobremesa)
        if prato not in ementa or bebida not in bebidas or sobremesa not in sobremesas:
            print("❌ Opção inválida!")
            pausa()
            return
    except ValueError:
        print("❌ Opção inválida!")
        pausa()
        return

    reservas.append({
        "codigo": cod,
        "data": data,
        "prato": ementa[prato],
        "bebida": bebidas[bebida],
        "sobremesa": sobremesas[sobremesa]
    })
    print("✅ Reserva efetuada!")
    pausa()

def listar_reservas_aluno():
    limpar_tela()
    print("📄 Página: Reservas do Aluno\n")
    listar_alunos_com_codigo()
    cod = input_ou_voltar("Código do aluno")
    if cod is None or not cod.isdigit():
        print("❌ Código inválido!")
        pausa()
        return
    cod = int(cod)

    encontrou = False
    for r in reservas:
        if r["codigo"] == cod:
            total = r["prato"]["preco"] + r["bebida"]["preco"] + r["sobremesa"]["preco"]
            print(f"{r['data']} - {r['prato']['nome']} + {r['bebida']['nome']} + {r['sobremesa']['nome']} (€{total:.2f})")
            encontrou = True
    if not encontrou:
        print("⚠️ Nenhuma reserva encontrada.")
    pausa()

def cancelar_reserva():
    limpar_tela()
    print("📄 Página: Cancelar Reserva\n")
    listar_alunos_com_codigo()
    cod = input_ou_voltar("Código do aluno")
    if cod is None or not cod.isdigit():
        print("❌ Código inválido!")
        pausa()
        return
    cod = int(cod)
    data = input_ou_voltar("Data da reserva (YYYY-MM-DD)")
    if data is None: return
    for r in reservas:
        if r["codigo"] == cod and r["data"] == data:
            reservas.remove(r)
            print("✅ Reserva cancelada!")
            pausa()
            return
    print("❌ Reserva não encontrada!")
    pausa()

def fatura_mensal():
    limpar_tela()
    print("📄 Página: Fatura Mensal\n")
    listar_alunos_com_codigo()
    cod = input_ou_voltar("Código do aluno")
    if cod is None or not cod.isdigit():
        print("❌ Código inválido!")
        pausa()
        return
    cod = int(cod)
    mes = input_ou_voltar("Mês da fatura (YYYY-MM, ex: 2026-03)")
    if mes is None: return
    total = 0
    for r in reservas:
        if r["codigo"] == cod and r["data"].startswith(mes):
            valor = r["prato"]["preco"] + r["bebida"]["preco"] + r["sobremesa"]["preco"]
            total += valor
            print(f"{r['data']} - €{valor:.2f}")
    print(f"\nTOTAL A PAGAR: €{total:.2f}")
    pausa()

# ---------------- MENU PRINCIPAL ----------------
def menu():
    while True:
        limpar_tela()
        print("=== CANTINA ESCOLAR ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Mostrar ementa")
        print("4. Fazer reserva")
        print("5. Listar reservas de um aluno")
        print("6. Mostrar fatura mensal")
        print("7. Cancelar reserva")
        print("8. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1": cadastrar_aluno()
        elif opcao == "2": listar_alunos()
        elif opcao == "3": 
            limpar_tela()
            mostrar_ementa()
            pausa()
        elif opcao == "4": fazer_reserva()
        elif opcao == "5": listar_reservas_aluno()
        elif opcao == "6": fatura_mensal()
        elif opcao == "7": cancelar_reserva()
        elif opcao == "8":
            print("👋 Programa encerrado.")
            break
        else:
            print("❌ Opção inválida.")
            pausa()

# ---------------- EXECUÇÃO ----------------
menu()

