from flask import Flask
from flask import render_template,request,redirect

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
  _FirstName = request.form["txtname"]
  _Surname = request.form["txtsurname"]
  _Email = request.form["txtemail"]
  _Phone = request.form["txtphone"]

  peopel = Peopel(_FirstName)
  peopel.surname = _Surname
  peopel.email = _Email
  peopel.phone = _Phone

  aux = ContactDao()
  aux.create(peopel)

  return redirect("/")


@app.route("/destroy/<string:id>")
def destroy(id):
  aux = ContactDao()
  aux.delete(id)
  return redirect("/")

@app.route("/update/<string:id>")
def update():
  
  pass



if __name__ == "__main__":
  app.run(debug=True)