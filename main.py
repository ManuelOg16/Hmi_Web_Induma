from flask import render_template,jsonify #importo funciones flash nos permite mandar mensajes entre vistas
import unittest
from sqlalchemy.orm import session # corredor de pruebas automatizadas
from app import create_app  # importo la funcion create_app
from  app.models.models import Hmi_t73, Hmi_t74
app = create_app()

@app.route('/')                       
def index():
    return  render_template('index.html')

@app.route('/pagina-dos')
def pagina_2():
 return render_template('pagina-dos.html')


@app.route('/troqueladora73', methods= ['GET',  'POST'])                       
def get_troqueladora73():
    try:
        variablesdb=Hmi_t73.query_troqueladora_73()
        on=variablesdb[1]
        reference=variablesdb[2]
        number_pieces=variablesdb[3]
        print(on,reference,number_pieces) 
    except TypeError:
        print("lista vacia datos nulos")
    except UnboundLocalError:
        print("sin datos para el json") 
    return jsonify(on=on,reference=reference,number_pieces=number_pieces) 
    

@app.route('/troqueladora74', methods= ['GET',  'POST'])                       
def get_troqueladora74():
    try:
        variablesdb=Hmi_t74.query_troqueladora_74()
        on=variablesdb[1]
        reference=variablesdb[2]
        number_pieces=variablesdb[3]
        print(on,reference,number_pieces) 
    except TypeError:
        print("lista vacia datos nulos")
    except UnboundLocalError:
        print("sin datos") 
    return jsonify(on=on,reference=reference,number_pieces=number_pieces) 
    

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)