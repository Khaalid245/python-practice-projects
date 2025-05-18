from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return  render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

app.run(debug=True)
