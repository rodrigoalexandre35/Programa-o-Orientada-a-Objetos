# Cadastro de alunos e notas (versão simples)

alunos = {
    "Ana": [8.5, 7.0, 9.2, 6.8],
    "Carlos": [5.5, 6.0, 7.5, 8.0],
    "Mariana": [9.0, 8.5, 10.0, 9.8],
    "Lucas": [6.5, 7.2, 5.8, 6.9],
    "Fernanda": [7.8, 8.2, 7.0, 8.5]
}

while True:
    print("\nMENU")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Mostrar alunos e notas")
    print("5 - Mostrar médias")
    print("6 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do aluno: ")
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Nota {i}: "))
            notas.append(nota)
        alunos[nome] = notas

    elif opcao == "2":
        nome = input("Nome do aluno: ")
        if nome in alunos:
            notas = []
            for i in range(1, 5):
                nota = float(input(f"Nova nota {i}: "))
                notas.append(nota)
            alunos[nome] = notas
        else:
            print("Aluno não encontrado!")

    elif opcao == "3":
        nome = input("Nome do aluno: ")
        if nome in alunos:
            del alunos[nome]
        else:
            print("Aluno não encontrado!")

    elif opcao == "4":
        for aluno, notas in alunos.items():
            print(aluno, ":", notas)

    elif opcao == "5":
        for aluno, notas in alunos.items():
            media = sum(notas) / 4
            print(aluno, "→ Média:", round(media, 2))

    elif opcao == "6":
        break

    else:
        print("Opção inválida!")
