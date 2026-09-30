nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    print("estudante cadastrado com sucesso!")

def calcular_media(indice):
    return (notas1[indice] + notas2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def listar():
    if len(nomes) == 0:
        print("Nenhum estudante cadastrado.")
        return

    print(f"\n{'Nome':<16} {'Nota 1':<7} {'Nota 2':<7} {'Média':<8} {'Situação':<14}")

    for i in range(len(nomes)):
        print(f"{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}"f"{calcular_media(i):<8.1f}{situacao(i):<14}")

def media_da_turma():
    if len(nomes) ==0:
        print("Nenhum estudante cadastrado.")
        return
    soma = 0

    for i in range (len(nomes)):
        soma = soma + calcular_media(i)
    print(f"\nMédia da turma: {soma/len(nomes):.2f}")

def menu():
    while True:
        print("\n1 - Cadasrar estudante")
        print("2 - Listar estudantes")
        print("3 - Média da turma")
        print("0 - sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            media_da_turma()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")
menu()

