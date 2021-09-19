from flask import Flask
#importamos el modulo de MySQL pde falsk
from flaskext.mysql import MySQL
from config.config import Conection

class Singleton(object):
  __instance = None

  def conectionBD(self,app:Flask):
    conect = Conection()
    self.mysql = MySQL()
    app.config["MySQL_DATABASE_USER"] = conect.user
    app.config["MYSQL_DATABASE_PASSWORD"] = conect.password
    app.config["MySQL_DATABASE_BD"] = conect.bd
    app.config["MySQL_DATABASE_HOST"] = conect.host
    self.mysql.init_app(app)
    self.conection = self.mysql.connect()
    self.cursor = self.conection.cursor()

  def __new__(cls):
    if Singleton.__instance is None:
      Singleton.__instance = object.__new__(cls)
    return Singleton.__instance