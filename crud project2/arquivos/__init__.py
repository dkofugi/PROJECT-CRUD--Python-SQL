import pandas as pd
import pyodbc


dados_conexao = (
    "DRIVER={MySQL ODBC 9.1 ANSI Driver};"
    "SERVER=localhost;"
    "PORT=3306;"
    "DATABASE=tarefas;"
    "UID=root;"
    "PWD=danilokofugi123;"
)



def verificararq():
    try:
        conexao = pyodbc.connect(dados_conexao)
        return conexao
    except pyodbc.Error as e:
        print(e)
        return None



def addArq(date, materia_,caderno ):
    conexao= verificararq()
    cursor=conexao.cursor()
    comando=f""" insert into tarefadf (data_atual, materia, caderno) 
    values
    ('{date}', '{materia_}', '{caderno}');"""
    cursor.execute(comando)
    cursor.commit()
    cursor.close()
    conexao.close()

    print("Tarefa adicionada!")


def exibirArq():
    comando = """SELECT tarefadf.id, tarefadf.data_atual, tarefadf.materia, GROUP_CONCAT(paginas.pagina SEPARATOR ', ') AS paginas, tarefadf.caderno
FROM tarefadf
JOIN paginas
ON tarefadf.id = paginas.id_tarefa
GROUP BY id_tarefa;"""
    conexao= verificararq()
    df= pd.read_sql(comando, conexao)
    df= df.to_string(index=False)
    conexao.close()
    print(df)
    return df


def removeArq():
    conexao= verificararq()
    exibirArq()
    cursor = conexao.cursor()
    while True:
        delete= int(input("QUAL TAREFA DESEJA REMOVER? Digite 999 para sair"))
        comando= f"""delete from tarefadf
    where id = {delete}
    LIMIT 1;"""
        cursor.execute(comando)
        cursor.commit()
        if delete == 999:
            break
        elif cursor.rowcount == 0:
            print("ESSA TAREFA NAO EXISTE! TENTE NOVAMENTE")
        else:
            try:
                cursor.execute(comando)
                cursor.commit()
                conexao.close()
            except:
                print("ERRO AO REMOCER TAREFA")
            else:
                print("TAREFA REMOVIDA COM SUCESSO!")
            break

def verificarCount():
    conexao= verificararq()
    comando="SELECT count(*) from tarefadf;"
    cursor= conexao.cursor()
    cursor.execute(comando)
    count= cursor.fetchone()
    conexao.close()
    for x in count:
        count= x
    return count

def last_id():
    conexao= verificararq()
    comando="""SELECT MAX(id) FROM tarefas.tarefadf"""
    cursor= conexao.cursor()
    cursor.execute(comando)
    id= cursor.fetchone()
    conexao.close()
    for x in id:
        id= x
    return id

def addPagina(paginas, id):
    conexao= verificararq()
    cursor= conexao.cursor()
    comando= f"""INSERT INTO paginas VALUES(DEFAULT, {paginas}, {id});"""
    cursor.execute(comando)
    cursor.commit()
    cursor.close()
    conexao.close()








