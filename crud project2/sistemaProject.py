import datetime
from interface import *
from arquivos import *
import time

conexao= verificararq()
if conexao:
    print("Conexão estabelecida com sucesso!")
    conexao.close()
    print("Conexao fechada!")
else:
    print("Nao foi possivel conectar com o banco de dados")



opcoes= ["ADICIONAR UMA TAREFA [1]", "EXIBIR TAREFAS [2]", "REMOVER UMA TAREFA [3]", "SAIR DO PROGRAMA [4]"]

while True:
    resp= menu(opcoes)
    if resp == 1:
        cabecalho('OPÇÃO 1')
        data=datetime.date.today()
        materia= input('QUAL MATERIA VOCE DESEJA ADICIONAR? ')
        y= leiaint('QUANTAS PAGINAS? ')
        pg= []
        for i in range(1, y + 1):
            pg.append(int(input(f"{i}ºpagina:  ")))
        caderno= input("TEM CADERNO? [S]/[N] ")
        addArq(data, materia, caderno)
        ultimo_id= last_id()
        for x in pg:
            pg = x
            addPagina(x, ultimo_id)
    elif resp == 2:
        cabecalho('OPÇÃO 2')
        exibirArq()
    elif resp == 3:
        cabecalho('OPÇÃO 3')
        removeArq()
    elif resp == 4:
        print('FINALIZANDO PROGRAMA', end='')
        for i in range(0, 3):
            print('.', end='')
            time.sleep(0.3)
        print()
        conexao= verificararq()
        cursor= conexao.cursor()
        cursor.close()
        break
    else:
        cabecalho('OPÇÃO INVALIDA TENTE NOVAMENTE')
print('VOLTE SEMPRE!')






