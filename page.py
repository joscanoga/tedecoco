import diagrama
import componente



class page:
    def __init__(self,df):
        self.df=df
        #print(df)
        self.id=df[df["parent"]=="1"]["id"].values[0]
        #print(df)
        componentes=df[df["parent"]==self.id].dropna()
        self.preguntas=[]
        for i in componentes.index:
            #valor=i[i["value"]=="configuracion"]
            if componentes["value"][i]=="configuracion" :
                self.configuracion=componente.configuracion(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df)
            else:
                #print( df[df["parent"] == componentes["id"][i]])
                self.preguntas.append(componente.pregunta(componentes["id"][i],componentes["parent"][i],componentes["value"][i],df))




page(diagrama.diagrama().sacar_componentes())
