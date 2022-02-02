import diagrama
import componente
import uuid
from data import dataBase as db
import json


class page:
    def __init__(self,df):
        self.df=df
        #print(df)
        self.id=df[df["parent"]=="1"]["id"].values[0]

        #print(df)
        componentes=df[df["parent"]==self.id].dropna()
        self.preguntas=[]
        contador=1
        for i in componentes.index:
            #valor=i[i["value"]=="configuracion"]
            if componentes["value"][i]=="configuracion" :
                self.configuracion=componente.configuracion(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df)
                #cadena=str(json.dumps(self.configuracion.ajustes))
                #print(cadena,type(cadena),self.idUrl)
                #db.addPage(self.idUrl,cadena)
            else:
                #print( df[df["parent"] == componentes["id"][i]])
                pregunta=componente.pregunta(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df,str(contador))
                contador+=1
                self.preguntas.append(pregunta)
                #print(json.dumps(pregunta.ajustes))
                #db.addPregunta(self.idUrl,json.dumps(pregunta.ajustes))

    def devolverPreguntas(self):
        preguntas=[]
        for i in self.preguntas:
            preguntas.append(i.ajustes["pregunta"])
        return preguntas


    def devolveridpregunta(self):
        preguntas = []
        for i in self.preguntas:
            preguntas.append(i.ajustes["id"])
        return preguntas

