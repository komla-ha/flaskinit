from flask_sqlalchemy import SQLAlchemy


class Config:
    pass

class ConfigProd:
    pass

class ConfigDev:
    debug = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLAlCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False