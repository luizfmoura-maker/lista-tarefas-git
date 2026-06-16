# ============================================================
#  LISTA DE TAREFAS — Atividade Rápida Git | SENAI
#  Você vai construir este programa função por função,
#  fazendo um commit a cada etapa concluída.
# ============================================================


# ------------------------------------------------------------
# JÁ PRONTO — Faça o commit inicial com este código
# ------------------------------------------------------------

tarefas = []  # lista que vai guardar as tarefas

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n===== LISTA DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Sair")
    print("============================")


# ------------------------------------------------------------
# VOCÊ VAI ADICIONAR AQUI — 1 função por commit
# ------------------------------------------------------------

# >> FUNÇÃO 2: adicionar_tarefa(descricao)
def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa à lista."""
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print(f'Tarefa "{descricao}" adicionada!')
# >> FUNÇÃO 3: listar_tarefas()
def listar_tarefas():
    """Lista todas as tarefas com seu status."""
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n--- Suas Tarefas ---")
    for i, tarefa in enumerate(tarefas, 1):
        status = "✅" if tarefa["concluida"] else "⬜"
        print(f"{i}. {status} {tarefa['descricao']}")
# >> FUNÇÃO 4: concluir_tarefa(numero)
def concluir_tarefa(numero):
    """Marca a tarefa do número informado como concluída."""
    if numero < 1 or numero > len(tarefas):
        print("Número de tarefa inválido.")
        return
    tarefas[numero - 1]["concluida"] = True
    print(f'Tarefa {numero} marcada como concluída!')
# >> FUNÇÃO 5: contar_pendentes()
def contar_pendentes():
    """Retorna o número de tarefas ainda pendentes."""
    pendentes = 0
    for tarefa in tarefas:
        if not tarefa["concluida"]:
            pendentes += 1
    return pendentes

# ------------------------------------------------------------
# ÁREA DE TESTES
# ------------------------------------------------------------

if __name__ == "__main__":
    exibir_menu()

    # Descomente conforme for adicionando as funções:
    # adicionar_tarefa("Estudar Git")
    # adicionar_tarefa("Fazer atividade")
    # listar_tarefas()
    # concluir_tarefa(1)
    # listar_tarefas()
    # print("Pendentes:", contar_pendentes())
