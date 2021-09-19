from model.peopel import Peopel
from flask import request

class ReceptionData():
  def __init__(self,name,surname,email,phone):
    self.peopel = Peopel(request.form[name])
    self.peopel.surname = request.form[surname]
    self.peopel.email = request.form[email]
    self.peopel.phone = request.form[phone]
  
  def getPerson(self):
    return self.peopel

