from flask import Flask, request, redirect , url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
app = Flask(__name__ , 
template_folder="views",
static_folder="public")
app.config["SECRET_KEY"] = "secrete"

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

class Disciplina(db.Model): 
    __tablename__ = "Disciplina" 
    id = db.Column(db.Integer, primary_key=True)
    Disciplina = db.Column(db.String(255), nullable=False)
    
    def __str__(self):
        return self.name

class Disc_Assunto(db.Model): 
    __tablename__ = "Disciplina_Assuntos" 
    id = db.Column(db.Integer, primary_key=True)
    Assunto = db.Column(db.String(124), nullable=False)
    Disciplina_Id = db.Column(db.Integer, db.ForeignKey("Disciplina.id"))

    def __str__(self):
        return self.name

class Exercicio(db.Model): 
    __tablename__ = "Exercicios" 
    Disciplina_Id = db.Column(db.Integer ,db.ForeignKey("Disciplina.id"))
    Disciplina_Assunto_ID = db.Column(db.Integer, db.ForeignKey("Disciplina_Assuntos.id"))
    Exe_Questoes_ID    = db.Column(db.Integer, primary_key=True)
    Exe_Questoes_Desc  = db.Column(db.String(255) , nullable=False)
    Exe_Questoes_Respostas    = db.Column(db.String(10) , nullable=False)
    Exe_Questoes_Solução      = db.Column(db.String(255) , nullable=False)

    def __str__(self):
        return self.name

class Exercicio(db.Model): 
    __tablename__ = "Exercicios_Alternativas" 
    Disciplina_Id = db.Column(db.Integer ,db.ForeignKey("Disciplina.id"))
    Disciplina_Assunto_ID = db.Column(db.Integer, db.ForeignKey("Disciplina_Assuntos.id"))
    Exe_Questoes_ID    = db.Column(db.Integer , db.ForeignKey("Exercicios.Exe_Questoes_ID"))
    Exe_Questoes_Alternativas_ID = db.Column(db.Integer, primary_key=True)
    Exe_Questoes_Alternativas = db.Column(db.String(255) , nullable=False)
 
    def __str__(self):
        return self.name


@app.route("/users")
def users():
    flash("Template USERS....")
    return render_template("users.html")

@app.route("/templates")
def templates():
    #return "<strong> Hello, World!</strong>"
    # utilizar render_template()
    #passando parametros para o template / criar dicionario User
    users= {
        "name":"Marcio villela",
        "idade":54,
        "email":"mpvillel5@gmail.com"
    }
    flash("Template....usuário criado com sucesso!")

    return render_template("templates.html", usersx=users)
    
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
