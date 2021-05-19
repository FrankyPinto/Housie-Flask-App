from flask import Flask
from flask import render_template, request, json
import random

app = Flask(__name__)

original_list = [1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,
41,42,43,44,45,46,47,48,49,50,
51,52,53,54,55,56,57,58,59,60,
61,62,63,64,65,66,67,68,69,70,
71,72,73,74,75,76,77,78,79,80,
81,82,83,84,85,86,87,88,89]

recent_num = []
numbers_called = []

# Client Home URL
@app.route("/")
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