import os
import uuid

from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect

from data import dataBase as db
from diagrama import diagrama
from forms.uploadFile import UploadForm
from page import page

app = Flask(__name__)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['get', 'post'])
def index():
    form = UploadForm()  # carga request.from y request.file
    if form.validate_on_submit():

        os.makedirs('data/xml', exist_ok=True)
        os.makedirs('data/resultados', exist_ok=True)
        f = form.xml.data

        filename = str(uuid.uuid4())
        filenameC = "data/xml/{}.xml".format(filename)
        f.save(filenameC)
        pagina = page(diagrama(filename).sacar_componentes())
        db.conexion().crearTablas(filename, pagina.devolverPreguntas())
        return redirect(url_for('form', id=filename))
    return render_template('index.html', form=form)


@app.route('/form/<id>', methods=["GET", "POST"])
def form(id):
    url = "{}.xml".format(str(id))
    pagina = page(diagrama(id).sacar_componentes())
    if request.method == 'POST':

        respuestas = []
        preguntas = pagina.devolverPreguntas()
        contador = 1
        for i in preguntas[:]:
            respuestas.append(request.form[str(contador) ])
            contador +=1
        #respuestas=dict(zip(preguntas, respuestas))
        db.conexion().addRespuesta(str(id),preguntas,respuestas)

        return redirect(url_for('respuesta'))
    return render_template("form.html", preguntas=pagina.preguntas,config=pagina.configuracion.ajustes)


@app.route("/respuesta")
def respuesta():
    return "respuesta guardada"


@app.route("/download/<id>")
def download(id):
    return("pagina en construccion")




if __name__ == '__main__':
    app.run(debug=True)



