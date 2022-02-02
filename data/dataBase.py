import sqlite3
def creartablas():
    conn = sqlite3.connect('Datos.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS page(id TEXT PRIMARY KEY, configuracion TEXT)")
    c.execute(
        "CREATE TABLE IF NOT EXISTS pregunta(id INTEGER PRIMARY KEY,idpage TEXT , ajustes TEXT, foreign key(idpage) references page(id))")
    conn.commit()
    c.close()
    conn.close()
def addPage(id,configuracion):
    conn = sqlite3.connect('Datos.db')
    c = conn.cursor()
    consulta="""INSERT INTO page VALUES (\'%s\',\'%s\')""" % (id, configuracion)
    #print(consulta)
    c.execute(consulta)
    #print("debug")
    conn.commit()
    c.close()
    conn.close()
def addPregunta(idpage,ajustes):
    conn = sqlite3.connect('Datos.db')
    c = conn.cursor()
    c.execute("""INSERT INTO pregunta( idpage, ajustes) 
                   VALUES (\'%s\',\'%s\')""" % (idpage, ajustes))
    conn.commit()
    c.close()
    conn.close()
creartablas()
