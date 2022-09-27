memoria = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

tabela_pagina = [[1,0,0],[2,0,0],[3,0,0],[4,0,0],[5,0,0],[6,0,0],[7,0,0],[8,0,0]]

import random

x = random.randint(0,7)

print(x)

def imprimir(tabela_pagina):
    print(" Processo ID |   Ref    |      Moldura   ")
    for l1 in range(len(tabela_pagina)):
        for c in range(3):
            print(tabela_pagina[l1][c], end='                ')
        print()
    print()

def imprimir_memoria(memoria):
    print(" Processo ID |   Ref    |      Moldura   ")
    for l1 in range(len(tabela_pagina)):
        for c in range(4):
            print(tabela_pagina[l1][c], end='                ')
        print()
    print()


def memoria_execucao(memoria,x):
    for i in range(4):
        if i == x:
            memoria[x][i] = 0
        else:
            memoria[x][i] = 0

def memoria_execucao_1(tabela_pagina,memoria,x):
        l = []
        m = random.randint(0, 3)
        if m in l:
            m = random.randint(0, 3)
        tabela_pagina[x][2] = m
        print(m,"quem é")
        imprimir(tabela_pagina)

def ref(tabela_pagina,memoria):
    for i in range(7):
        x = random.randint(0, 7)
        tabela_pagina[x][1] = 1
        print(x,"quem x")
        #imprimir(tabela_pagina)
        memoria_execucao_1(tabela_pagina,memoria,x)




imprimir(tabela_pagina)
ref(tabela_pagina,memoria)