import sqlite3
import pandas as pd

# funcion para crear y/o devolver la base de datos
# recibe un id que es el nombre de la base de datos
# devuelve un cursor de la base de datos
class conexion:

    def crearDB(self,id):
        conn = sqlite3.connect('data/resultados/{}.db'.format(id))
        return conn


# funcion para crear la tabla para el formulario
    def crearTablas(self,id, preguntas):
        conn = sqlite3.connect('data/resultados/{}.db'.format(id))
        c = conn.cursor()
        print
        preguntasColumnas = ""
        for i in preguntas:
            preguntasColumnas += ", '{}' text ".format(i)
        consult="CREATE TABLE IF NOT EXISTS '{}'(id INTEGER PRIMARY KEY {})".format(id, preguntasColumnas)

        c.execute(consult)
        conn.commit()
        c.close()
        conn.close()

    def addRespuesta(self, idtabla,preguntas, respuestas,idform=None):
        if idform is None:
            idform=idtabla
        conn = sqlite3.connect('data/resultados/{}.db'.format(idform))
        c = conn.cursor()

        preguntasColumnas = ""
        respuestasColumnas=""
        for i in   range(len(preguntas)):
            preguntasColumnas += " ,'{}'".format(preguntas[i])
            respuestasColumnas += " ,'{}'".format(respuestas[i])

        consult = "INSERT INTO '{}'({}) values ({});".format(idtabla, preguntasColumnas[2:],respuestasColumnas[2:])
        print(consult)

        c.execute(consult)
        conn.commit()
        c.close()
        conn.close()

    def getRespuesta(self, idtabla, respuestas, idform=None):

        if idform is None:
            idform = idtabla
        respuestas.insert(0,"index")
        filename='data/resultados/{}.db'.format(idform)
        print(filename)
        conn = sqlite3.connect(filename)
        c = conn.cursor()

        consult = "SELECT * FROM '{}';".format(idtabla)
        print(consult)

        c.execute(consult)
        records = c.fetchall()
        df=pd.DataFrame(records,columns=respuestas)
        df.set_index("index",inplace=True)
        print(df)
        conn.commit()
        c.close()
        conn.close()




