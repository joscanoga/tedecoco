import estructura_xml
import xml.etree.ElementTree as ET


class diagrama:


    def __init__(self):
        self.file=estructura_xml.leer_estructura_basica()
        print("hola")


    def sacar_componentes(self):
        print(self.file)
        for i in self.file:
            for j in i.findall("mxCell"):
                print(j.get("parent") )


d= diagrama()
d.sacar_componentes()
"""<root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-1" value="Página Principal" style="swimlane;" parent="1" vertex="1">
          <mxGeometry x="20" y="10" width="740" height="300" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-2" value="Nuevo" style="swimlane;horizontal=0;startSize=23;" parent="UQa_-jZZVjBJoI7FMsdu-1" vertex="1">
          <mxGeometry x="20" y="50" width="200" height="200" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-5" value="Categorías" style="swimlane;horizontal=0;startSize=23;" parent="UQa_-jZZVjBJoI7FMsdu-1" vertex="1">
          <mxGeometry x="520" y="50" width="200" height="200" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-6" value="Secciones" style="swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;" parent="1" vertex="1">
          <mxGeometry x="580" y="80" width="140" height="90" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-7" value="Damas" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;" parent="UQa_-jZZVjBJoI7FMsdu-6" vertex="1">
          <mxGeometry y="30" width="140" height="30" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-8" value="Caballeros" style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;" parent="UQa_-jZZVjBJoI7FMsdu-6" vertex="1">
          <mxGeometry y="60" width="140" height="30" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-10" value="Caballeros" style="swimlane;" parent="1" vertex="1">
          <mxGeometry x="60" y="500" width="290" height="280" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-11" value="Damas" style="swimlane;startSize=23;" parent="1" vertex="1">
          <mxGeometry x="470" y="500" width="310" height="280" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-12" value="&lt;div&gt;Selecciona&lt;/div&gt;&lt;div&gt;Categoría&lt;br&gt;&lt;/div&gt;" style="rhombus;whiteSpace=wrap;html=1;" parent="1" vertex="1">
          <mxGeometry x="340" y="350" width="120" height="130" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-13" value="" style="endArrow=classic;html=1;rounded=0;exitX=0.508;exitY=1.006;exitDx=0;exitDy=0;exitPerimeter=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" parent="1" source="UQa_-jZZVjBJoI7FMsdu-8" target="UQa_-jZZVjBJoI7FMsdu-12" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="610" y="410" as="sourcePoint" />
            <mxPoint x="660" y="360" as="targetPoint" />
            <Array as="points">
              <mxPoint x="651" y="350" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-14" value="&lt;div&gt;Cliente&lt;/div&gt;&lt;div&gt;Escoge&lt;/div&gt;&lt;div&gt;Cateogoría&lt;br&gt;&lt;/div&gt;" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;" parent="1" vertex="1">
          <mxGeometry x="600" y="350" width="70" height="50" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-15" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="UQa_-jZZVjBJoI7FMsdu-12" target="UQa_-jZZVjBJoI7FMsdu-10" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="390" y="420" as="sourcePoint" />
            <mxPoint x="440" y="370" as="targetPoint" />
            <Array as="points">
              <mxPoint x="205" y="415" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-16" value="&lt;div&gt;Selecciona&lt;/div&gt;&lt;div&gt;Caballeros&lt;/div&gt;" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;" parent="1" vertex="1">
          <mxGeometry x="210" y="430" width="70" height="30" as="geometry" />
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-17" value="" style="endArrow=classic;html=1;rounded=0;entryX=0.75;entryY=0;entryDx=0;entryDy=0;exitX=1;exitY=0.5;exitDx=0;exitDy=0;" parent="1" source="UQa_-jZZVjBJoI7FMsdu-12" target="UQa_-jZZVjBJoI7FMsdu-11" edge="1">
          <mxGeometry width="50" height="50" relative="1" as="geometry">
            <mxPoint x="350" y="425" as="sourcePoint" />
            <mxPoint x="215" y="510" as="targetPoint" />
            <Array as="points">
              <mxPoint x="703" y="415" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="UQa_-jZZVjBJoI7FMsdu-18" value="&lt;div&gt;Selecciona&lt;/div&gt;Damas" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;" parent="1" vertex="1">
          <mxGeometry x="615" y="430" width="70" height="30" as="geometry" />
        </mxCell>
      </root>"""