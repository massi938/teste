import time
from datetime import datetime

def criar_lista():
    lista_processo = [[1, "", 0.35, 3], [2, "", 0.25, 1],
                      [3, "", 0.25, 2], [4, "", 0.15, 1]
                      , [5, "", 0.15, 4], [6, "", 0.15, 1]
                      , [7, "", 0.15, 3], [8, "", 0.15, 2]]
    for i in range(len(lista_processo)):
        data_e_hora_atuais = datetime.now()
        a = data_e_hora_atuais.strftime("%H:%M:%S")
        lista_processo[i][1] = a
        time.sleep(2)
    imprimir(lista_processo)
    prioridade(lista_processo)

def imprimir(lista_processo):
    print(" Processo ID | Tempo de Entrada | Tempo de Execução | Prioridade")
    for l1 in range(len(lista_processo)):
        for c in range(4):
            print(lista_processo[l1][c], end='               ')
        print()
    print()


def prioridade(lista_processo):

    b = 0
    for l1 in range(len(lista_processo)):
        if lista_processo[l1][3] > 1:
            if lista_processo[l1][3] > b:
                b = lista_processo[l1][3]
                pr = l1

    if b != 0:
        execucao(lista_processo,pr)
        prioridade(lista_processo)
    else:
        tempo_de_entrada(lista_processo)

def tempo_de_entrada(lista_processo):
    b = 24
    for l1 in range(len(lista_processo)):
        data_e_hora = lista_processo[l1][1]
        data_e_hora = (data_e_hora.replace(":", ".", 1))
        data_e_hora = (data_e_hora.replace(":", "", 1))
        #print(data_e_hora)
        a = float(data_e_hora)
        if a < 24:
            if a < b:
                b = a
                pr = l1
    execucao_final(lista_processo, pr)

def execucao_final(lista_processo,pr):
    lista_processo.pop(pr)
    if len(lista_processo) == 0:
        print("Processo finalizado")
    else:
        imprimir(lista_processo)
        tempo_de_entrada(lista_processo)


def execucao(lista_processo,pr):
    #lista_processo.pop(pr)
    lista_processo[pr][3] -= 1
    imprimir(lista_processo)


criar_lista()