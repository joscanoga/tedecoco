import pandas as pd
import estructura_xml


class diagrama:


    def __init__(self,filename="Proyecto_Tedecoco.drawio"):
        self.file=estructura_xml.leer_estructura_basica(filename)



    def sacar_componentes(self):
        #print(self.file)
        df=pd.DataFrame(columns=["id","parent","value"])
        for i in self.file:
            for j in i.findall("mxCell"):
                id=j.get("id")
                parent=j.get("parent")
                value=j.get("value")
                df.loc[len(df.index)] =[id,parent,value]
                #df=df.append({"id":id,"parent":parent,"value":value}, ignore_index=True)

        return df

