import time
from datetime import datetime

def criar_lista():
    lista_processo = [[1, "", 15, 3], [2, "", 5, 1],
                      [3, "", 10, 2], [4, "", 5, 1]
                  ]
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
            print(f'{lista_processo[l1][c]:^5}', end='             ')
        print()
    print()

def imprimir_execução(lista_processo,pr):
    data_e_hora_atuais = datetime.now()
    a = data_e_hora_atuais.strftime("%H:%M:%S")
    print("Processo executado ")
    print()
    print("Hora de Entrada: ",a)

    print(" Processo ID | Tempo de Entrada | Tempo de Execução | Prioridade")
    for c in range(4):
        print(f'{lista_processo[pr][c]:^5}', end='             ')
    print()
    time.sleep(5)
    data_e_hora_atuais = datetime.now()
    a = data_e_hora_atuais.strftime("%H:%M:%S")
    #print()
    print("Hora de saida: ", a)
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
    imprimir_execução(lista_processo, pr)
    lista_processo.pop(pr)
    if len(lista_processo) == 0:
        print("Processo finalizado")
    else:

        imprimir(lista_processo)
        tempo_de_entrada(lista_processo)


def execucao(lista_processo,pr):
    #lista_processo.pop(pr)
    imprimir_execução(lista_processo, pr)
    lista_processo[pr][3] -= 1
    lista_processo[pr][2] -= 5

    imprimir(lista_processo)


criar_lista()