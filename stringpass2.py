from flask import Flask,jsonify
import pickle
with open("stringpass.pkl","rb") as sp:
    data=pickle.load(sp)


app=Flask(__name__)
@app.route("/")
def home():
        fruits=["apple","mango","banana"]
        count=[i for i in range(3)]
        fruitdict=dict(zip(count,fruits))
        # fruitdict=dict.fromkeys(fruits,"in stock")   Method will produce dict with all fruits as key and all stock as value
        return jsonify(fruitdict)
        # return jsonify(data)


if __name__=="__main__":
    app.run(debug=True)

