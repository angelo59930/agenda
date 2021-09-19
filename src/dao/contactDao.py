from flask import Flask
from patterns.singleton import Singleton
from model.peopel import Peopel

class ContactDao:
  
  def __init__(self):
    self.bd = Singleton()
    

  def create(self,peopel:Peopel):
    INSERT_CONTACT = "INSERT INTO Agenda.peopel (idpeopel,name,surname,phone,email) VALUES (%s,%s,%s,%s,%s)"
    data = (peopel.id,peopel.name,peopel.surname,peopel.phone,peopel.email)
    self.bd.cursor.execute(INSERT_CONTACT,data)
    self.bd.conection.commit()
  
  def delete(self,id):
    DELETE_COMTACT = "DELETE FROM Agenda.peopel WHERE idpeopel=%s"
    self.bd.cursor.execute(DELETE_COMTACT,id)
    self.bd.conection.commit()
    