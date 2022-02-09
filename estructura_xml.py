
import xml.etree.ElementTree as ET




def leer_estructura_basica(filename="Proyecto_Tedecoco"):
    # leemos el xml
    file = ET.parse("data/xml/{}.xml".format(filename)).getroot()
    #estraemos el diagrama
    return file.findall("diagram/mxGraphModel/")
