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
        self.ajustes=dict()
        for i in hijos.index:
            x=re.findall(r"(^.*) : (.*)",hijos["value"][i])[0]
            self.ajustes[x[0]]=x[1]


class pregunta(componente):
    def __init__(self, id, parent, value, df):
        componente.__init__(self, id, parent, value)
        hijos = df[df["parent"] == self.id]
        for i in hijos.index:

            if hijos["value"][i]=="":
                hijos=hijos.drop([i])
        self.ajustes = dict()
        for i in hijos.index:
            x = re.findall(r"(^.*) : (.*)", hijos["value"][i])[0]
            self.ajustes[x[0]] = x[1]
        #print(self.ajustes)


#class abierta(pregunta):