from flask import Flask, request, redirect , url_for, render_template
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
#Bootstrap(app)

@app.route("/")
def index():
    return "<a href='/posts'>Posts</a>"

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
