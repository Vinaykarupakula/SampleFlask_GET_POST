from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/content', methods=['GET'])
def diaplay():
    if request.method=='GET':
        print("Hello")
        return jsonify({"Message":"This is sample message value"})

@app.route('/math', methods=['POST','GET'])
def calc():
    if request.method == 'POST':
        name = request.json['name']
        uid = request.json['uid']
        if (str(name).isupper() and len(str(uid))==10):
            return jsonify({"data":[
                {name:uid}
            ]})
        return jsonify({'message':'invalid data'})


if __name__ == '__main__':
    app.run(debug=False)

