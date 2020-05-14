from flask import Flask, request, redirect , url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db=SQLAlchemy(app)

class User(db.Model): 
    __tablename__ = "users" 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)
    profile = db.relationship('Profile', backref='User', uselist=False)



    def __str__(self):
        return self.name

class Profile(db.Model): 
    __tablename__ = "Profiles" 
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(124), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))



    def __str__(self):
        return self.name

@app.route("/")
def index():
    users = User.query.all() # Select * from users;
    #return "<a href='/posts'>Posts x</a>"
    return render_template("users.html",users=users)

@app.route("/user/delete/<int:id>")
def delete(id):
    user =User.query.filter_by(id=id).firts()
    db.session.delete(user)
    db.session.commit()

    return redirect("/")

@app.route("/user/<int:id>")
def unique(id):
    user =User.query.get(id)
    return render_template("user.html",user=user)

@app.route("/response")
def response():
    #return "Um resposta do servidor"  #comentado para utilizar render_template
    return  render_template("response.html")

@app.route("/redirect")
def redirect2():
 #   return redirect("/response")
    return redirect(url_for("response"))

@app.route("/posts")   # decorator
def posts():
    Data = dict(
        path=request.path,
        referrer=request.referrer,
        Content=request.content_type,
        method=request.method
    )
    return Data 


    
if __name__ == '__main__':
    app.run(debug=True)
