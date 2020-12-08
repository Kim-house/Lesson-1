from flask import Flask
app = Flask(__name__)
@app.route("/")

def hello():
    return "Hello World"
if__name__=='__main__':
app.run(debug)
