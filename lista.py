import time

from datetime import date

from datetime import datetime

lista_processo = [[1,"",0.35,3],[2,"",0.25,1],
                  [3,"",0.25,2],[4,"",0.15,1]]




def imprimir(lista_processo):
    print(" Processo ID | Tempo de Entrada | Tempo de Execução | Prioridade")
    for l1 in range(len(lista_processo)):
        for c in range(4):
            print(lista_processo[l1][c], end='                 ')
        print()
    print()



lista =[]
for i in range(4):
    data_e_hora_atuais = datetime.now()
    a = data_e_hora_em_texto = data_e_hora_atuais.strftime("%H:%M:%S")
    lista_processo[i][1] = a
    lista.append(a)
    time.sleep(2)
print(lista_processo)

'''print(data_e_hora_em_texto)
data_e_hora = (data_e_hora_em_texto.replace(":",".",1))
data_e_hora = (data_e_hora.replace(":","",1))
print(data_e_hora)
z = float(data_e_hora)'''

for i in range(4):
    #print(lista[i])
    data_e_hora = lista[i]
    data_e_hora = (data_e_hora.replace(":", ".", 1))
    data_e_hora = (data_e_hora.replace(":", "", 1))
    print(data_e_hora)
print(lista)
''