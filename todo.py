import redis

db = redis.Redis(
    host = "localhost",
    port = 6379,
    db = 0,
    decode_responses = True
)

def adicionar_tarefa(tarefa:str):
    db.lpush("todo", tarefa)
    print(f"Tarefa adicionada: {tarefa}")

def listar_tarefas():
    tarefas = db.lrange("todo", 0, -1)
    if not tarefas:
        print("Nenhuma tarefa encontrada")
        return
    
    print("\n----Lista de tarefas----")
    for k, v in enumerate(tarefas, start=1):
        print(f"{k}: {v}")
    print("-------------------------\n")

def remover_tarefa(numero:int):
    tarefas = db.lrange("todo", 0, -1)
    if numero < 1 or numero > len(tarefas):
        print("Número Inválido")
        return

    tarefa = tarefas[numero -1]
    db.lrem("todo", 1, tarefa)
    print(f"Tarefa removida: {tarefa}")

def menu():
    while True:
        print("1 - Adicionar Tarefa")
        print("2 - Listar Tarefas")
        print("2 - Remover Tarefa")
        print("4 - Finalizar Programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tarefa = input("Digite uma tarefa: ")
            adicionar_tarefa(tarefa)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            numero = int(input("Digite o número da tarefa que deseja remover: "))
            remover_tarefa(numero)
        elif opcao == "4":
            return False

menu()