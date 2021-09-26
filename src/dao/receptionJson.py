from model.peopel import Peopel

class ReceptionJson():
  def __init__(self,person):
    self.peopel = Peopel(person["name"])
    self.peopel.surname =  person["surname"]
    self.peopel.email = person["email"]
    self.peopel.phone = person["phone"]

  def getPerson(self):
    return self.peopel