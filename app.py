from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, from a github application inside the original application!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=8080)
