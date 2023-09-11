from flask import Flask, render_template, redirect, url_for, request
from pymongo import MongoClient
from db import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
@app.route('/AM', methods=['GET'])
def AM():
    AM = obtener_AM()
    form = buscar_registrosAM("")
    return render_template('AM.html', AM=AM, form=form)

@app.route('/AM/reproducirAM/<AM_id>')
def reproducirAM(AM_id):
    AM = collectionAM.find_one({'nombre': AM_id})  # Obtener el registro de la emisora seleccionada
    if AM:
        # Renderizar la plantilla HTML para los controles de reproducción
        return render_template('reproducirAM.html', AM=AM)
    else:
        # Emisora no encontrada, redireccionar a la página principal
        return render_template('error.html')

@app.route('/FM', methods=['GET'])
def FM():
    FM = obtener_FM()
    form = buscar_registrosFM("")
    return render_template('FM.html', FM=FM, form=form)

@app.route('/FM/reproducirFM/<FM_id>')
def reproducirFM(FM_id):
    FM = collectionFM.find_one({'nombre': FM_id})  # Obtener el registro de la emisora seleccionada
    if FM:
        # Renderizar la plantilla HTML para los controles de reproducción
        return render_template('reproducirFM.html', FM=FM)
    else:
        # Emisora no encontrada, redireccionar a la página principal
        return render_template('error.html')

@app.route('/Mundial', methods=['GET'])
def Mundial():
    Mundial = obtener_Mundo()
    form = buscar_registrosMundo("")
    return render_template('Mundial.html', Mundial=Mundial, form=form)

@app.route('/Mundial/reproducirMundial/<Mundial_id>')
def reproducirMundial(Mundial_id):
    Mundial = collectionMundial.find_one({'nombre': Mundial_id})  # Obtener el registro de la emisora seleccionada
    if Mundial:
        # Renderizar la plantilla HTML para los controles de reproducción
        return render_template('reproducirMundial.html', Mundial=Mundial)
    else:
        # Emisora no encontrada, redireccionar a la página principal
        return render_template('error.html')

@app.route('/Musica', methods=['GET'])
def Musica():
    Musica = obtener_Musica()
    return render_template('Musica.html', Musica=Musica)

@app.route('/Musica/reproducirMusica/<Musica_id>')
def reproducirMusica(Musica_id):
    Musica = collectionMusica.find_one({'nombre': Musica_id})  # Obtener el registro de la emisora seleccionada
    if Musica:
        # Renderizar la plantilla HTML para los controles de reproducción
        return render_template('reproducirMusica.html', Musica=Musica)
    else:
        # Emisora no encontrada, redireccionar a la página principal
        return render_template('error.html')
    
@app.route('/resultadoAM', methods=['POST'])
def resultadoAM():
    termino_busqueda = request.form['termino_busqueda']
    # Utiliza la función buscar_registros desde db.py
    resultados = buscar_registrosAM(termino_busqueda)
    return render_template('resultadoAM.html', resultados=resultados)

@app.route('/resultadoFM', methods=['POST'])
def resultadoFM():
    termino_busqueda = request.form['termino_busqueda']
    # Utiliza la función buscar_registros desde db.py
    resultados = buscar_registrosFM(termino_busqueda)
    return render_template('resultadoAM.html', resultados=resultados)

@app.route('/resultadoMundo', methods=['POST'])
def resultadoMundo():
    termino_busqueda = request.form['termino_busqueda']
    # Utiliza la función buscar_registros desde db.py
    resultados = buscar_registrosMundo(termino_busqueda)
    return render_template('resultadoAM.html', resultados=resultados)

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    app.run(debug=True)
