from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_mail import Mail, Message


app = Flask(__name__)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"]= "smtp.gmail.com"
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"]= "sheekhxareed9900@gmail.com"
app.config["MAIL_PASSWORD"]= "jfxfjtqypjhcudjn"
mail = Mail(app)
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name, email=email,
                    date=date_obj, occupation=occupation)

        db.session.add(form)         # ✅ Save the form
        db.session.commit()         # ✅ Commit the changes
        message_body = f"""
        Dear {first_name} {last_name},

        Thank you for your recent submission. We have received your application successfully.

        Our team will carefully review the details you have provided. You can expect a follow-up email regarding the status of your application shortly.

        If you have any questions or need further assistance, feel free to reply to this email.

        Best regards,  
        Application Review Team  
        📧 sheekhxareed9900@gmail.com
        """

        message = Message(subject="New form application",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body
                          )
        mail.send(message)
        flash(f"{first_name}, your form was submitted successfully", "success")

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=50001)
