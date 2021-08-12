from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello!!!</h1> <br><h5>This is a sample app using flask</h5><br><br><h6>Created by<br>Akash Thawait</h6>"

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5000, debug = True) 