lista_processo = [[1,15.31,0.35,3],[2,15.33,0.25,1],
                  [3,15.41,0.25,2],[4,15.42,0.15,1]]



def imprimir(lista_processo):
    print(" Processo ID | Tempo de Entrada | Tempo de Execução | Prioridade")
    for l1 in range(len(lista_processo)):
        for c in range(4):
            print(lista_processo[l1][c], end='                 ')
        print()
    print()


def prioridade(lista_processo):

    b = 0
    for l1 in range(len(lista_processo)):
        if lista_processo[l1][3] > 1:
            if lista_processo[l1][3] > b:
                b = lista_processo[l1][3]
                #print(lista_processo[l1][3] > b," ",l1)
                pr = l1

    if b != 0:
        #tempo_de_entrada(lista_processo)
        execucao(lista_processo,pr)
        prioridade(lista_processo)
    else:

        tempo_de_entrada(lista_processo)
    #imprimir(lista_processo)

def tempo_de_entrada(lista_processo):
    b = 24
    for l1 in range(len(lista_processo)):
        if lista_processo[l1][1] < 24:
            if lista_processo[l1][1] < b:
                b = lista_processo[l1][1]
                #print(lista_processo[l1][1] ," ",l1)
                pr = l1
    execucao_final(lista_processo, pr)

def execucao_final(lista_processo,pr):
    lista_processo.pop(pr)
    imprimir(lista_processo)



def execucao(lista_processo,pr):
    lista_processo.pop(pr)
    #lista_processo[pr][3] -= 1

    #lista_processo[pr][1] += (lista_processo[pr][2])
    imprimir(lista_processo)


imprimir(lista_processo)
prioridade(lista_processo)