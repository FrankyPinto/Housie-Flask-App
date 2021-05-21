from flask import Flask
from flask import render_template, request, json, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "housie-flask-app"

original_list = list(range(1,90))

recent_num = []
numbers_called = []

@app.route("/")
def home():
    return render_template("loginpage.html")

@app.route("/loginapi", methods=['POST'])
def login_api():
    if "user_client" in session:
        return redirect(url_for("homepage"))
    elif "user_admin" in session:
        return redirect(url_for("adminhome"))
    elif request.method == "POST":
        uname = request.form['u_name']
        upwd = request.form['u_paswd']
        if uname=="client" and upwd=="client":
            session["user_client"] = uname
            return redirect(url_for("homepage"))
        elif uname=="admin" and upwd=="admin":
            session["user_admin"] = uname
            return redirect(url_for("adminhome"))
        else:
            return render_template("errortemp.html")
        print(uname,upwd)
    else:
        return render_template("errortemp.html")

@app.route("/logout")
def logout():
    if "user_client" in session:
        session.pop("user_client",None)
        return redirect(url_for("home"))
    elif "user_admin" in session:
        session.pop("user_admin",None)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

# Client Home URL
@app.route("/clienthome")
def homepage():
    return render_template("clienthome.html")

# Client Home API
@app.route("/clientapi", methods=['POST'])
def clientapi():
    return json.dumps({'status':'OK','number_called':recent_num[0],'number_list':numbers_called})

# Admin Home URL
@app.route("/adminpanel")
def adminhome():
    return render_template("adminhome.html")

# Admin Home API
@app.route("/adminapi", methods=['POST'])
def adminapi():
    print("request recieved")
    x = random.choice(original_list)
    recent_num.clear()
    recent_num.append(x)
    numbers_called.append(x)
    original_list.remove(x)
    print(x,"--",recent_num,"--",numbers_called)
    return json.dumps({'status':'OK','numcalled':x,'numlist':numbers_called})

if __name__ == "__main__":
    app.run()