from uuid import uuid1

class Peopel:
  def __init__(self,name):
    self.name = name
    self.surname = "empty"
    self.phone = "empty"
    self.email = "empty"
    self.id = uuid1()

  def __str__(self) -> str:
    return self.surname + " " + self.name
