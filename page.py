import diagrama
import componente
import uuid
from data import dataBase as db
import json


class page:
    def __init__(self,df):
        self.df=df
        self.id=df[df["parent"]=="1"]["id"].values[0]


        componentes=df[df["parent"]==self.id].dropna()
        self.preguntas=[]
        contador=1
        for i in componentes.index:

            if componentes["value"][i]=="configuracion" :
                self.configuracion=componente.configuracion(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df)
            else:

                pregunta=componente.pregunta(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df,str(contador))
                contador+=1
                self.preguntas.append(pregunta)



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



