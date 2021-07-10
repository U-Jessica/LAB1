import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    name1=jsonObj['name1']
    name2=jsonObj['name2']
    response+="<b> Welcome <b>"+name1+" "+name2+"</b> to the IC100 Class<br>"
    a=int(jsonObj['a'])
    b=int(jsonObj['b'])
    c=int(jsonObj['c'])
    ans1=a+b+c
    response+="<b> Sum of a,b,c is: <b>"+str(ans1)+"</b><br>"
    ans2=(a*b)/c
    response+="<b> (a*b)/c: <b>"+str(ans2)+"</b><br>"
    	    
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
