from flask import Flask, render_template

from diagrama import diagrama
from page import  page
app = Flask(__name__)

@app.route('/')
def index():
    pagina=page(diagrama().sacar_componentes())

    return render_template("index.html",preguntas=pagina.preguntas)



if __name__ == '__main__':
    app.run(debug=True)