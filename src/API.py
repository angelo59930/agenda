from flask import Flask,json
from flask import request,jsonify

from model.peopel import Peopel
from patterns.singleton import Singleton
from dao.contactDao import ContactDao
from dao.receptionJson import ReceptionJson


#Declaramos la app
app = Flask(__name__)

app.secret_key="supersecretvalidation"

#Conection to data base
bd = Singleton()
bd.conectionBD(app)

#inicializacion del dao
contact = ContactDao()

@app.route("/")
def index():
  sql = "SELECT * FROM Agenda.peopel;"
  bd.cursor.execute(sql)
  peopel =  bd.cursor.fetchall()
  bd.conection.commit()
  return jsonify(peopel)
  #return render_template("contacs/index.html",peopel=peopel)

@app.route("/add-contact",methods=["POST"])
def storage():
  tmp = ReceptionJson(person=request.json)
  contact.create(tmp.getPerson())
  return request.json

@app.route("/remove-contact/<string:id>",methods=["DELETE"])
def destroy(id):
  contact.delete(id)
  return  jsonify({"message":"person removed succesfuly"})

@app.route("/update-contact/<string:id>",methods=["PUT"])
def edit(id):
  person = request.json
  aux = Peopel(person["name"])
  aux.surname = person["surname"]
  aux.email = person["email"]
  aux.phone = person["phone"]
  contact.update(aux,id)
  return jsonify({"message":"person updated succesfuly"})




if __name__ == "__main__":
  app.run(debug=True)