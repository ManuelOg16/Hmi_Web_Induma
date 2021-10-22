import pyodbc
import csv
from time import time
from time import sleep
from datetime import datetime
from datetime import timedelta

class DataBase:
    def __init__(self):
        try:
            #self.connection = pyodbc.connect('DRIVER={SQL Server}; SERVER={192.168.18.101};DATABASE={INDUMAPLTESORITO}; UID={SA};PWD={Induma21}')   
            self.connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER={DESKTOP-CT1VGTN};DATABASE={hmi_induma};UID={sa};PWD={Virolo2021$}')
            print(" - DATABASE: conexión exitosa")
    
        except Exception as e:
            print("Ocurrió un error al conectar a SQL Server: ", e)

    def insert_dataframe(self,troquel):
        sql = 'INSERT INTO dbo.hmi_troqueladora_{} (datee,onn,reference_1,number_pieces) VALUES (getdate(),1,22,26)'.format(troquel)
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.connection.commit()
                print(" - DATABASE: There was inserted 1 dataframe")
        except Exception as e:
            raise
    def  delete_all(self,troquel):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM dbo.hmi_troqueladora_{}".format(troquel)
                cursor.execute(sql)
                self.connection.commit()
                print(" - DATABASE: Table troqueladora_{} was emptied".format(troquel))
        except Exception as e:
                    raise

    

