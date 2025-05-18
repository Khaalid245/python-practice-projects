from Tools.scripts.objgraph import definitions
from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return  render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def contact(station,date):
    temperature = 23
    return {"station":station,
            "date":date,
            "temperature":temperature
            }


if __name__ == "__main__":
    app.run(debug=True, port=5002)
