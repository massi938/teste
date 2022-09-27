#Paulo Rafael Ribeiro dos Santos 609382
#Richard Hiroshi da Silva Nishizaki 590541
#Thiago Massi da Costa 590576

import os
def limpar():
    os.system('cls')

def menu():
    while True:
        print("             Projeto Autômato Finito Determinístico (AFD) ")
        print("Digite:")
        print('''[1] - Criar autômato:\n[2] - Sair''')
        select = (input(" "))
        if select == '1':
            menu1()
        if select == '2':
            break

def menu1():
    limpar()
    a = " "
    while True:
        print()
        print("Digite:")
        print('''[1] - Verificar palavra:
[2] - Implementar as funcionalidades do autômato:
[3] - Sair''')
        select = (input(" "))

        if select == '1':
            if a == " ":
                print("Alfabeto não existe ")
            else:
                print("Palavra válida precisa ter uma sequência de "+ a1)
                print()
                Verificar_palavra_1(a1)

        if select == '2':
            limpar()
            a = input("Informe o alfabeto:").upper()
            q = int(input("Quantidade de estados: "))
            a1 = input("Infome A palavra que sera necessario para validar o automato ").upper()
            criar_tabela_1(a, q, a1)

        if select == '3':
            break


def criar_tabela_1(a,q,a1):
    tabela = []
    i = 0
    i1 = 0
    print()
    print("crie a tabela de trasição com  a palavra valida: " + a1)
    for l in range(q + 1):
        tabela.append([])
        for c in range(len(a) + 1):

            if l == 0 and c != 0:
                tabela[l].append(a[i])
                i += 1

            elif l != 0 and c == 0:
                tabela[l].append("Q" + str(i1))
                i1 += 1


            elif c == 0 and l == 0:
                tabela[l].append(" ")

            else:
                print()
                tabela[l].append(input("A linha " + str(tabela[l][0]) + " Coluna " + str(tabela[0][c]) + ":"))
                print(str(tabela[l]))

    print()
    for l in range(q + 1):
        for c in range(len(a) + 1):
            print(f'[{tabela[l][c]:^5}]', end='')
        print()
    print()
    return

def Verificar_palavra_1(a1):
    while True:
        v = input("Verificar palavra:").upper()
        if (v.count(a1)):
            print("Palavra Valida")
        else:
            print("Palavra Invalida")
        s = input('''Digite 1 para sair: 
Ou ENTER para verificar outra palavra:''')
        if s == '1':
            break

menu()