from flask import Flask
from flask import render_template,request,redirect
from dao.receptionData import ReceptionData

from patterns.singleton import Singleton
from model.peopel import Peopel
from dao.contactDao import ContactDao


#Declaramos la app
app = Flask(__name__)

#Conection to data base
bd = Singleton()
bd.conectionBD(app)

@app.route("/")
def index():
  sql = "SELECT * FROM Agenda.peopel;"
  bd.cursor.execute(sql)
  peopel =  bd.cursor.fetchall()

  bd.conection.commit()

  return render_template("contacs/index.html",peopel=peopel)

@app.route("/create")
def create():
  return render_template("contacs/create.html")

@app.route("/store",methods=["POST"])
def storage():
  person = ReceptionData("txtname","txtsurname","txtemail","txtphone")
  aux = ContactDao()
  aux.create(person.getPerson())

  return redirect("/")


@app.route("/destroy/<string:id>")
def destroy(id):
  aux = ContactDao()
  aux.delete(id)
  return redirect("/")

@app.route("/update/<string:id>")
def edit(id):
  aux = ContactDao()
  peopel = aux.read(id)

  return render_template("contacs/edit.html",peopel=peopel)

@app.route("/update",methods=["POST"])
def update():
  person = ReceptionData("txtname","txtsurname","txtemail","txtphone")

  return redirect("/")


if __name__ == "__main__":
  app.run(debug=True)