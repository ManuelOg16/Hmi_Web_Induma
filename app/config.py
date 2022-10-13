import urllib.parse 
import os
from sqlalchemy import create_engine
class Config:
    ### modificar la configuracion 
    ENV= 'development' # para trabajar en modo desarrollador
    params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-9KBS3V2\SQLEXPRESS;DATABASE=hmi_induma;UID=**;PWD=***")
    SQLALCHEMY_DATABASE_URI =  "mssql+pyodbc:///?odbc_connect=%s" % params
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    engine = create_engine('mssql+pyodbc:///?odbc_connect=%s' % params) 
