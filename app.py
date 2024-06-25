from flask import Flask as fl, request, render_template

app = fl(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/submit', methods=['POST','GET'])
def calcular():
    if request.method == "POST":
        a = int(request.form["Valora"])
        b = int(request.form["Valorb"])
        c = int(request.form["Valorc"])

        discr = (b**2)-(4*a*c)
        res1 = (-b+(discr**1/2))/2*a
        res2 = (-b-(discr**1/2))/2*a

        return render_template("index.html", res1=res1, res2=res2, Valora=a, Valorb=b, Valorc=c)

if __name__ =="__main__":
    app.run(debug=True,port=5000)

