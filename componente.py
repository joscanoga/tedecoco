import regex as re

class componente:
    def __init__(self,id,parent,value):
        self.id=id
        self.parent=parent
        self.value=value




class configuracion(componente):
    def __init__(self,id,parent,value,df):
        componente.__init__(self,id,parent,value)
        hijos=df[df["parent"]==self.id]
        self.ajustes={"fondo": "formulario","titulo" : "blue","fuente" : "arial","colorFuente" : "green","max-width" : "1000px","justificacion" : "center","text-align" : "center"}
        for i in hijos.index:
            x=re.findall(r"(\S.+\S)\s*:\s*(\S.+\S)",hijos["value"][i])[0]
            self.ajustes[x[0]]=x[1]
        if self.ajustes["justificacion"]=="center":
            self.ajustes["justificacion"]="margin: 0 auto;justify-content:center;"
        elif self.ajustes["justificacion"]=="right":
            self.ajustes["justificacion"]="position: absolute;right: 5px"
        elif self.ajustes["justificacion"]=="left":
            self.ajustes["justificacion"]="position: absolute;left: 5px"

class pregunta(componente):
    def __init__(self, id, parent, value, df,id2):
        componente.__init__(self, id, parent, value)
        hijos = df[df["parent"] == self.id]
        for i in hijos.index:

            if hijos["value"][i]=="":
                hijos=hijos.drop([i])
        self.ajustes = dict()
        self.ajustes["value"]=value

        for i in hijos.index:
            x = re.findall(r"(\S.+\S)\s*:\s*(\S.+\S)", hijos["value"][i])[0]
            self.ajustes[x[0]] = x[1]
        #print(self.ajustes)
        self.ajustes["id"]=id2

#class abierta(pregunta):