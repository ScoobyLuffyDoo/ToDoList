from flask import Flask, jsonify,request
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/MyToDoList'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'a15s#%^a1A@Q$'

db = SQLAlchemy(app)

class Todolist(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    item=db.Column(db.String(100))

    def __init__(self,item):
        self.item = item


@app.route("/search", methods=['GET'])
def Search_to_do_items():
    if request.method == 'GET':
        reference = request.args.get('reference') 
        respond =[]
        try:
            if reference:
                response = Todolist.query.filter(Todolist.item.like('%{}%'.format(reference)))
                for result in response:
                    respond.append(result.item)  
                context = json.dumps(respond, indent=2)
            else:
                response = db.session.query(Todolist).all()  
                for result in response:
                    respond.append(result.item)
                context = json.dumps(respond, indent=2)    
        except:
            response = "No Data"
            context = json.dumps(response, indent=2)
    return context


@app.route("/addToDoItem", methods=['POST'])
def Add_to_do_items():
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            item_data = request_data["item"]        
            entry = Todolist(item_data)
            db.session.add(entry)
            db.session.commit()
            response =  "Record Added"
        except:    
            response =  "Record Not Added"
    return jsonify({'message':response})

if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)