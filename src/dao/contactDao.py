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
    DELETE_CONTACT = "DELETE FROM Agenda.peopel WHERE idpeopel=%s"
    self.bd.cursor.execute(DELETE_CONTACT,id)
    self.bd.conection.commit()

  def read(self,id):
    SELECT_CONTACT = "SELECT * FROM Agenda.peopel WHERE idpeopel = %s"
    self.bd.cursor.execute(SELECT_CONTACT,id)
    peopel = self.bd.cursor.fetchall()
    self.bd.conection.commit()
    return peopel
  
  def readAll(self):
    SELECT_ALL_CONTACT = "SELECT * FROM Agenda.peopel"
    self.bd.cursor.execute(SELECT_ALL_CONTACT)
    peopel = self.bd.cursor.fetchall()
    self.bd.conection.commit()
    return peopel

  def update(self,peopel:Peopel,id):
    UPDATE_CONTACT = "UPDATE Agenda.peopel SET name=%s,surname=%s,phone=%s,email=%s WHERE idpeopel=%s"
    data = (peopel.name,peopel.surname,peopel.phone,peopel.email,id)
    self.bd.cursor.execute(UPDATE_CONTACT,data)
    self.bd.conection.commit()
    