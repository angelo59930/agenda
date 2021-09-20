from flask import Flask
from flask import render_template,request,url_for,flash,redirect
from dao.receptionData import ReceptionData

from patterns.singleton import Singleton
from model.peopel import Peopel
from dao.contactDao import ContactDao


#Declaramos la app
app = Flask(__name__)

app.secret_key="supersecretvalidation"

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
  name = request.form["txtname"]
  if name == "":
    flash("The name of contact is nessesary")
    return redirect(url_for("create"))
    
  person = ReceptionData("txtname","txtsurname","txtemail","txtphone")
  aux = ContactDao()
  aux.create(person.getPerson())

  return redirect("/")


@app.route("/destroy/<string:id>")
def destroy(id):
  aux = ContactDao()
  aux.delete(id)
  return redirect("/")

@app.route("/edit/<string:id>")
def edit(id):
  aux = ContactDao()
  peopel = aux.read(id)

  return render_template("contacs/edit.html",peopel=peopel)

@app.route("/update",methods=["POST"])
def update():
  _id = request.form["txtId"]
  aux = ReceptionData("txtname","txtsurname","txtemail","txtphone")
  cDao = ContactDao()
  cDao.update(aux.getPerson(),_id) 
  return redirect("/")


if __name__ == "__main__":
  app.run(debug=True)