from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class test(db.Model):
    email = db.Column(db.String(200), primary_key=True)
    firstname = db.Column(db.String(200), nullable=False)
    lastname = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.email} - {self.firstname} - {self.lastname}"


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/registration", methods=['GET', 'POST'])
def registraion():

    if request.method == 'POST':
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        attendees = test.query.all()
        for attendee in attendees:
            if attendee.email == email:
                return render_template('registration.html', find=True)
        attendee = test(email=email, firstname=firstname, lastname=lastname)
        db.session.add(attendee)
        db.session.commit()
    return render_template('registration.html', find=False)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/attendees")
def atendees():
    # attendee = test(email="mayank@mail.com",firstname="mayank", lastname="giri")
    # db.session.add(attendee)
    # db.session.commit()
    attendees = test.query.all()
    # print(attendees)
    return render_template('attendees.html', attendees=attendees)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
