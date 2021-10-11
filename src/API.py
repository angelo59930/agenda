from flask import Flask,json
from flask import request,jsonify
from flask_cors import CORS

from model.peopel import Peopel
from patterns.singleton import Singleton
from dao.contactDao import ContactDao
from dao.receptionJson import ReceptionJson


#Declaramos la app
app = Flask(__name__)

app.secret_key="supersecretvalidation"

CORS(app)

#Conection to data base
bd = Singleton()
bd.conectionBD(app)

#inicializacion del dao
contact = ContactDao()

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

@app.route("/search/<string:id>",methods=["GET"])
def func(id):
  return jsonify(contact.read(id))

@app.route("/contacts",methods=["GET"])
def contacts():
  return jsonify(contact.readAll())

if __name__ == "__main__":
  app.run()