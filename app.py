import uuid
import pandas as pd

from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename, redirect

from diagrama import diagrama
from forms.uploadFile import UploadForm
from page import page

app = Flask(__name__)
import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['get', 'post'])
def index():
    form = UploadForm()  # carga request.from y request.file
    if form.validate_on_submit():
        f = form.xml.data

        filename = str(uuid.uuid4())
        filenameC = "data/xml/{}.xml".format(filename)
        f.save(filenameC)
        pagina = page(diagrama(filename).sacar_componentes())
        df = pd.DataFrame(columns=pagina.devolverPreguntas())
        df.to_excel('data/resultados/{}.xlsx'.format(filename))
        return redirect(url_for('form', id=filename))
    return render_template('index.html', form=form)


@app.route('/form/<id>', methods=["GET", "POST"])
def form(id):
    url = "{}.xml".format(str(id))
    pagina = page(diagrama(id).sacar_componentes())
    if request.method == 'POST':
        df = pd.read_excel('data/resultados/{}.xlsx'.format(id))
        respuestas = []
        preguntas = pagina.devolverPreguntas()
        contador = 1
        for i in preguntas[:]:
            respuestas.append(request.form[str(contador) ])
            contador +=1
        respuestas=dict(zip(preguntas, respuestas))
        df=df.append(respuestas, ignore_index=True)
        df=df[preguntas]
        df.to_excel('data/resultados/{}.xlsx'.format(id))

        return redirect(url_for('respuesta'))
    return render_template("form.html", preguntas=pagina.preguntas,config=pagina.configuracion.ajustes)


@app.route("/respuesta")
def respuesta():
    return "respuesta guardada"


if __name__ == '__main__':
    app.run(debug=True)
