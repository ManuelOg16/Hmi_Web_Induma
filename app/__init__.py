from flask import Flask #vamos a importar el objeto Flask que es el objeteo principal del Framework.
from flask_bootstrap import Bootstrap #importamos boostrap para fronted
from .config import Config   #importamos desde el archivo .config la clase Config
from  app.models.models import db, migrate

def create_app():
    app = Flask(__name__)  #Ahora vamos a crear una aplicación Flask, para ello instanciamos el objeto Flask
    bootstrap = Bootstrap(app)

    #db.init_app(app) #la base de datos se inicialice en la app
    migrate.init_app(app, db)  # Se inicializa el objeto migrate

    #app.config.from_object(Config)

    if Config is None:
        app.config.from_object(Config.BaseConfig)
    else:
        app.config.from_object(Config)
    db.init_app(app)
    

    return app