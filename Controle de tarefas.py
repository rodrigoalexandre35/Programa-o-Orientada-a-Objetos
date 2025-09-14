# Lista de tarefas
tarefas = []

while True:
    print("\nMENU")
    print("1 - Adicionar tarefa")
    print("2 - Concluir tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Título: ")
        desc = input("Descrição: ")
        tarefas.append({"titulo": titulo, "descricao": desc, "status": "Pendente"})

    elif opcao == "2":
        for i, t in enumerate(tarefas):
            print(i, "-", t["titulo"], "(", t["status"], ")")
        n = int(input("Número da tarefa: "))
        tarefas[n]["status"] = "Concluído"

    elif opcao == "3":
        print("\nPendentes:")
        for t in tarefas:
            if t["status"] == "Pendente":
                print("-", t["titulo"])
        print("\nConcluídas:")
        for t in tarefas:
            if t["status"] == "Concluído":
                print("-", t["titulo"])

    elif opcao == "4":
        break
