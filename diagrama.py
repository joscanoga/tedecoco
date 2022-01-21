import estructura_xml
import xml.etree.ElementTree as ET
import pandas as pd

class diagrama:


    def __init__(self):
        self.file=estructura_xml.leer_estructura_basica()



    def sacar_componentes(self):
        print(self.file)
        df=pd.DataFrame(columns=["id","parent","value"])
        for i in self.file:
            for j in i.findall("mxCell"):
                id=j.get("id")
                parent=j.get("parent")
                value=j.get("value")
                df=df.append({"id":id,"parent":parent,"value":value}, ignore_index=True)

        return df

