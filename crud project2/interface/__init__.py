from winotify import Notification
def cabecalho(txt):
    largura= len(txt) + 8
    print("-" * largura)
    print(txt.center(largura))
    print("-" * largura)


def menu(opc):
    cabecalho('MENU PRINCIPAL')
    for x in opc:
        print(f'{x}')
    opcao= leiaint("OPÇAO: ")
    return opcao



def leiaint(num):
    while True:
        try:
            num = int(input(num))
        except ValueError:
            print("ERRO! DIGITE UM NUMERO VALIDO:  ")
        except KeyboardInterrupt:
            print()
            print("O usuario preferiu nao digitar o numero")
        else:
            return num


def notification(count):
    notificacao= Notification(app_id="Lembrete", title="Tarefa Dom Felipe",
                              msg=f"{count} Tarefas não realizadas!", duration="short")
    notificacao.show()
