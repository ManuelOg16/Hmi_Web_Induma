from flask import request, make_response, redirect, render_template, url_for, flash #importo funciones flash nos permite mandar mensajes entre vistas
import unittest # corredor de pruebas automatizadas
from app import create_app  # importo la funcion create_app
from  app.models.models import db
app = create_app()

@app.route('/')                       
def index():                           
    return  render_template('index.html')


if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)