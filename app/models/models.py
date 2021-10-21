from sqlalchemy.orm import backref
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
from app.config import Config



db = SQLAlchemy()
migrate = Migrate()  # Se crea un objeto de tipo Migrate
engine= Config.engine


class Hmi_t73(db.Model):
    __tablename__ = 'hmi_troqueladora_73'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datee= db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    onn = db.Column(db.Boolean)
    reference_1 = db.Column(db.Integer)
    number_pieces = db.Column(db.Integer)

    
    def query_troqueladora_73():
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="SELECT datee,onn,reference_1,number_pieces FROM hmi_troqueladora_73"
        register=cursor.execute(sql)
        register = cursor.fetchone()
        daTedb=register[0]
        oNdb=register[1]
        refeRence_1db=register[2]
        number_piEces =register[3]
        register = cursor.fetchone()
        db.session.commit()
        listdb=[daTedb,oNdb,refeRence_1db,number_piEces]
        return listdb

    
class Hmi_t74(db.Model):
    __tablename__ = 'hmi_troqueladora_74'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datee= db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    onn = db.Column(db.Boolean)
    reference_1 = db.Column(db.Integer)
    number_pieces = db.Column(db.Integer)

    
    def query_troqueladora_74():
        connection = engine.raw_connection()
        cursor = connection.cursor()
        sql="SELECT datee,onn,reference_1,number_pieces FROM hmi_troqueladora_74"
        register=cursor.execute(sql)
        register = cursor.fetchone()
        daTedb=register[0]
        oNdb=register[1]
        refeRence_1db=register[2]
        number_piEces =register[3]
        register = cursor.fetchone()
        db.session.commit()
        listdb=[daTedb,oNdb,refeRence_1db,number_piEces]
        return listdb
    
 
    