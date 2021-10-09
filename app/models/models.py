from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime

db = SQLAlchemy()
migrate = Migrate()  # Se crea un objeto de tipo Migrate


class Hmis(db.Model):
    __tablename__ = 'hmi_troqueladora_73'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha= db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    funcionando = db.Column(db.Boolean, nullable=False)
    parada = db.Column(db.Boolean, nullable=False)
    referencia_1 = db.Column(db.Boolean, nullable=False)
    referencia_2 = db.Column(db.Boolean, nullable=False)
    referencia_3 = db.Column(db.Boolean, nullable=False)
    numero_piezas = db.Column(db.Integer)
    