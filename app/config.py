class Config:
    ### modificar la configuracion 
    ENV= 'development' # para trabajar en modo desarrollador
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:@127.0.0.1/taskapp' #llamar las credenciales de mariadb con SQLALQUEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False