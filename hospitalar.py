import os
from datetime import datetime

# ---------------- FUNÇÕES DE TELA ----------------
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa(msg="\nPressione ENTER para continuar..."):
    input(msg)

# ---------------- DADOS ----------------
pacientes = []
consultas = []

id_paciente_atual = 1
id_consulta_atual = 1

# ---------------- FUNÇÕES AUXILIARES ----------------
def nome_paciente(id_p):
    for p in pacientes:
        if p["id"] == id_p:
            return p["nome"]
    return "Desconhecido"

# ---------------- VALIDAÇÕES ----------------
def validar_idade(idade_str):
    if not idade_str.isdigit():
        return None
    idade = int(idade_str)
    if 0 <= idade <= 120:
        return idade
    return None

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return data_str
    except ValueError:
        return None

def validar_hora(hora_str):
    try:
        datetime.strptime(hora_str, "%H:%M")
        return hora_str
    except ValueError:
        return None

def validar_contacto(contacto_str):
    # Apenas números, máximo 15 dígitos
    if contacto_str.isdigit() and 1 <= len(contacto_str) <= 15:
        return contacto_str
    return None

# ---------------- PACIENTES ----------------
def cadastrar_paciente():
    global id_paciente_atual
    limpar_tela()
    print("📄 Página: Cadastrar Paciente")
    print("Digite 'V' a qualquer momento para voltar ao menu principal.\n")

    nome = input("Nome do paciente: ")
    if nome.strip().upper() == "V":
        return

    while True:
        idade_str = input("Idade: ")
        if idade_str.strip().upper() == "V":
            return
        idade = validar_idade(idade_str)
        if idade is None:
            print("❌ Idade inválida! Deve ser um número entre 0 e 120.")
        else:
            break

    while True:
        contacto = input("Contacto (apenas números, max 15 dígitos): ")
        if contacto.strip().upper() == "V":
            return
        if validar_contacto(contacto):
            break
        else:
            print("❌ Contacto inválido! Use apenas números e máximo 15 dígitos.")

    paciente = {"id": id_paciente_atual, "nome": nome, "idade": idade, "contacto": contacto}
    pacientes.append(paciente)
    id_paciente_atual += 1
    print("\n✅ Paciente cadastrado com sucesso!")
    pausa()

def listar_pacientes():
    limpar_tela()
    print("📄 Página: Lista de Pacientes\n")
    if not pacientes:
        print("⚠️ Nenhum paciente registado.")
    else:
        print(f"{'ID':<5}{'Nome':<20}{'Idade':<5}{'Contacto':<15}")
        print("-"*50)
        for p in pacientes:
            print(f"{p['id']:<5}{p['nome']:<20}{str(p['idade']):<5}{p['contacto']:<15}")
    pausa()

def eliminar_paciente():
    while True:
        limpar_tela()
        print("📄 Página: Eliminar Paciente")
        print("Digite 'V' para voltar ao menu principal.\n")

        if not pacientes:
            print("⚠️ Nenhum paciente disponível.")
            pausa()
            return

        print(f"{'ID':<5}{'Nome':<20}{'Idade':<5}{'Contacto':<15}{'Status':<15}")
        print("-"*70)
        for p in pacientes:
            status = "Com consultas" if any(c["id_paciente"] == p["id"] for c in consultas) else "Livre"
            print(f"{p['id']:<5}{p['nome']:<20}{str(p['idade']):<5}{p['contacto']:<15}{status:<15}")

        print()
        id_input = input("ID do paciente a eliminar: ")
        if id_input.strip().upper() == "V":
            return
        try:
            id_p = int(id_input)
        except ValueError:
            print("❌ Por favor, digite um número válido.")
            pausa()
            continue

        if any(c["id_paciente"] == id_p for c in consultas):
            print("❌ Não é possível eliminar o paciente. Existem consultas marcadas.")
            pausa()
            continue

        for p in pacientes:
            if p["id"] == id_p:
                pacientes.remove(p)
                print("✅ Paciente eliminado com sucesso.")
                pausa()
                return
        else:
            print("❌ Paciente não encontrado.")
            pausa()

# ---------------- CONSULTAS ----------------
def marcar_consulta():
    global id_consulta_atual
    limpar_tela()
    print("📄 Página: Marcar Consulta")
    print("Digite 'V' a qualquer momento para voltar ao menu principal.\n")

    if not pacientes:
        print("⚠️ Nenhum paciente disponível.")
        pausa()
        return

    while True:
        print("Pacientes disponíveis:")
        print(f"{'ID':<5}{'Nome':<20}{'Idade':<5}{'Contacto':<15}")
        print("-"*50)
        for p in pacientes:
            print(f"{p['id']:<5}{p['nome']:<20}{str(p['idade']):<5}{p['contacto']:<15}")
        print()

        id_input = input("ID do paciente: ")
        if id_input.strip().upper() == "V":
            return
        try:
            id_paciente = int(id_input)
        except ValueError:
            print("❌ Por favor, digite um número válido.")
            continue

        if not any(p["id"] == id_paciente for p in pacientes):
            print("❌ Paciente não existe.")
            continue

        while True:
            data = input("Data (YYYY-MM-DD): ")
            if data.strip().upper() == "V":
                return
            if validar_data(data):
                break
            else:
                print("❌ Data inválida! Formato correto: YYYY-MM-DD")

        while True:
            hora = input("Hora (HH:MM): ")
            if hora.strip().upper() == "V":
                return
            if validar_hora(hora):
                break
            else:
                print("❌ Hora inválida! Formato correto: HH:MM")

        tipo = input("Tipo de consulta: ")
        if tipo.strip().upper() == "V":
            return

        estado = "Marcada"

        consulta = {
            "id": id_consulta_atual,
            "id_paciente": id_paciente,
            "data": data,
            "hora": hora,
            "tipo": tipo,
            "estado": estado
        }
        consultas.append(consulta)
        id_consulta_atual += 1
        print(f"\n✅ Consulta marcada com sucesso! (Estado: {estado})")
        pausa()
        return

# ---------------- RESTANTE DAS FUNÇÕES ----------------
def listar_consultas():
    limpar_tela()
    print("📄 Página: Lista de Consultas\n")
    if not consultas:
        print("⚠️ Nenhuma consulta registada.")
    else:
        print(f"{'ID':<5}{'Paciente ID':<12}{'Nome':<20}{'Data':<12}{'Hora':<6}{'Tipo':<15}{'Estado':<10}")
        print("-"*80)
        for c in consultas:
            print(f"{c['id']:<5}{c['id_paciente']:<12}{nome_paciente(c['id_paciente']):<20}{c['data']:<12}{c['hora']:<6}{c['tipo']:<15}{c['estado']:<10}")
    pausa()

def consultas_por_paciente():
    limpar_tela()
    print("📄 Página: Consultas do Paciente\n")
    print("Digite 'V' para voltar ao menu principal.\n")

    if not pacientes:
        print("⚠️ Nenhum paciente disponível.")
        pausa()
        return

    print(f"{'ID':<5}{'Nome':<20}{'Idade':<5}{'Contacto':<15}")
    print("-"*50)
    for p in pacientes:
        print(f"{p['id']:<5}{p['nome']:<20}{str(p['idade']):<5}{p['contacto']:<15}")
    print()

    id_input = input("ID do paciente: ")
    if id_input.strip().upper() == "V":
        return
    try:
        id_p = int(id_input)
    except ValueError:
        print("❌ ID inválido.")
        pausa()
        return

    encontrou = False
    print(f"\nConsultas do paciente: {nome_paciente(id_p)}\n")
    for c in consultas:
        if c["id_paciente"] == id_p:
            print(f"ID Consulta: {c['id']} | {c['data']} {c['hora']} | {c['tipo']} | {c['estado']}")
            encontrou = True
    if not encontrou:
        print("⚠️ Nenhuma consulta encontrada para este paciente.")
    pausa()

def proxima_consulta():
    limpar_tela()
    print("📄 Página: Próxima Consulta\n")
    print("Digite 'V' para voltar ao menu principal.\n")

    if not pacientes:
        print("⚠️ Nenhum paciente disponível.")
        pausa()
        return

    print(f"{'ID':<5}{'Nome':<20}{'Idade':<5}{'Contacto':<15}")
    print("-"*50)
    for p in pacientes:
        print(f"{p['id']:<5}{p['nome']:<20}{str(p['idade']):<5}{p['contacto']:<15}")
    print()

    id_input = input("ID do paciente: ")
    if id_input.strip().upper() == "V":
        return
    try:
        id_p = int(id_input)
    except ValueError:
        print("❌ ID inválido.")
        pausa()
        return

    futuras = []
    for c in consultas:
        if c["id_paciente"] == id_p and c["estado"].lower() == "marcada":
            data_hora = datetime.strptime(c["data"] + " " + c["hora"], "%Y-%m-%d %H:%M")
            futuras.append((data_hora, c))

    if not futuras:
        print("⚠️ Nenhuma consulta futura encontrada.")
        pausa()
        return

    futuras.sort()
    c = futuras[0][1]
    print(f"📅 Próxima consulta de {nome_paciente(id_p)}: {c['data']} {c['hora']} | {c['tipo']}")
    pausa()

def alterar_estado_consulta():
    limpar_tela()
    print("📄 Página: Alterar Estado da Consulta\n")
    print("Digite 'V' para voltar ao menu principal.\n")

    if not consultas:
        print("⚠️ Nenhuma consulta disponível para alterar.")
        pausa()
        return

    print(f"{'ID':<5}{'Paciente':<20}{'Data':<12}{'Hora':<6}{'Tipo':<15}{'Estado':<10}")
    print("-"*70)
    for c in consultas:
        print(f"{c['id']:<5}{nome_paciente(c['id_paciente']):<20}{c['data']:<12}{c['hora']:<6}{c['tipo']:<15}{c['estado']:<10}")
    print()

    id_input = input("ID da consulta: ")
    if id_input.strip().upper() == "V":
        return
    try:
        id_c = int(id_input)
    except ValueError:
        print("❌ ID inválido.")
        pausa()
        return

    for c in consultas:
        if c["id"] == id_c:
            print(f"Consulta do paciente: {nome_paciente(c['id_paciente'])}")
            novo_estado = input("Novo estado: ")
            if novo_estado.strip().upper() == "V":
                return
            c["estado"] = novo_estado
            print("✅ Estado da consulta atualizado.")
            pausa()
            return

    print("❌ Consulta não encontrada.")
    pausa()

# ---------------- MENU PRINCIPAL ----------------
def menu():
    while True:
        limpar_tela()
        print("=== SISTEMA HOSPITALAR ===")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Marcar consulta")
        print("4. Listar consultas")
        print("5. Ver consultas de um paciente")
        print("6. Ver próxima consulta de um paciente")
        print("7. Alterar estado da consulta")
        print("8. Eliminar paciente")
        print("9. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1": cadastrar_paciente()
        elif opcao == "2": listar_pacientes()
        elif opcao == "3": marcar_consulta()
        elif opcao == "4": listar_consultas()
        elif opcao == "5": consultas_por_paciente()
        elif opcao == "6": proxima_consulta()
        elif opcao == "7": alterar_estado_consulta()
        elif opcao == "8": eliminar_paciente()
        elif opcao == "9":
            print("👋 Programa encerrado.")
            break
        else:
            print("❌ Opção inválida.")
            pausa()

# ---------------- EXECUÇÃO ----------------
menu()
