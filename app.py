from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80),unique = True,nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return "HEllo"

@app.route('/drinks')
def get_drinks():
    drinks = Drinks.query.all()
    output =[]
    for d in drinks:
        drink_data = {"name": d.name,"description" : d.description}
        output.append(drink_data)
    return  {"drinks" : output}

@app.route('/drinks/<id>')
def get_drink(id):
    d= Drinks.query.get_or_404(id)
    return {"name": d.name,"description" : d.description}

@app.route('/drinks', methods=["POST"])
def add_drink():
    drink= Drinks(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}

@app.route('/drinks/<id>', methods=["DELETE"])
def delete_drink(id):
    d= Drinks.query.get(id)
    if d is None:
        return {"error": "not found"}
    db.session.delete(d)
    db.session.commit()
    return {"Message":"Deleted"}