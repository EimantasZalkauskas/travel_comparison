import requests
from flask import Flask, render_template

app = Flask(__name__)

url = "http://api.aviationstack.com/v1/flights"
params = {
    "access_key": "5d80b6b40b9d20f2d8064df230f88300"
}


@app.get("/")
def home():
    response = requests.get(url, params)
    print(response.status_code)
    return render_template("index.html", resp=response)



