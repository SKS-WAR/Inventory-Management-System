from flask import Flask,redirect,url_for, render_template, request,send_file,session
try:
    import sendDataToFirebase
except :
    pass
import webbrowser
import desktopNotification
import firebaseAPI_handler
import sendDataToFirebase
from datetime import date
import date_time

app = Flask(__name__)
app.secret_key = "BIGsecretOfMine&plzDontDecrptMe"

@app.route("/",methods=["POST","GET"])
@app.route("/login",methods=["POST","GET"])
def login():
    if 'user' in session:
        return redirect(url_for('product'))
    if request.method == "POST":
        name = request.form["uname"]
        password = request.form["password"]
        user = firebaseAPI_handler.login(name,password)
        session['user'] = user
        if user != None :
            return redirect(url_for("home"))
        else:
            return render_template('login.html')
    else:
        return render_template("login.html")

@app.route('/landing')
@app.route('/home')
def home():
    if 'user' in session:
        return render_template('landing.html')
    return redirect(url_for('login'))

@app.route("/bottlesempty")
def bottles_empty():
    return render_template("bottles_empty.html")
    
@app.route("/bottlesfilled")
def bottles_filled():
    return render_template("bottles_filled.html")



@app.route("/product",methods=["POST","GET"])
def product():
    if 'user' in session:
        user = session["user"]
        if request.method == "POST":
            dt = date_time.get_current_date()
            product_name = request.form["product"]
            units = request.form["units"]
            price = request.form["price"]
            #sending data to firebase
            try:
                firebaseAPI_handler.sendFilledBottlesProductionData(auth=user,name=product_name,date=dt,price=price,quantity=units)
                desktopNotification.notify("Data Inserted successfully")
            except :
                desktopNotification.notify("Some Issues Arised")
            return redirect(url_for("product"))
        else:
            return render_template("index.html")
    else:
        return redirect(url_for('login'))

@app.route("/user")
def user():
    if 'user' in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))

@app.route("/despatch",methods=["POST","GET"])
def despatch():
    if 'user' in session:
        user = session["user"]
        if request.method == "POST":
            d = date_time.get_current_date()
            p_name = request.form["product"]
            unts = request.form["units"]
            amount = request.form["price"]
            #sending data to firebase
            try:
                firebaseAPI_handler.sendFilledBottlesDespatchData(auth=user,name=p_name,date=d,price=amount,quantity=unts)
                desktopNotification.notify("Data Inserted successfully")
            except :
                desktopNotification.notify("Some Issues Arised")
            return redirect(url_for("despatch"))
        else:
            return render_template("despatch.html")
    else:
        return redirect(url_for('login'))


@app.route('/query',methods=["GET","POST"])
def query():
    if 'user' in session:
        user = session["user"]
        if request.method == "POST":
            user = session["user"]
            
            month = request.form["month"]
            total,total_prod,total_dep =  firebaseAPI_handler.bottlesFilledBottles_calc_month(user,month)
            
            #a = "Sudeep"
            #b = "Sahoo"
            return redirect(url_for("display",total=total, t_prod=total_prod ,t_dept=total_dep))
        else:
            return render_template("query.html")
    else:
        return redirect(url_for('login'))   

#to download a file use <a href = "{{url_for('download_report')}}">Download</a>
@app.route("/download")
def download():
    return render_template("download.html")
	
@app.route("/xyz")
def download_report():
    path = "robots.txt"
    return send_file(path,as_attachment=True)

@app.route("/logout")
def logout():
    session.pop('user',None)
    return redirect(url_for('login'))

@app.route('/result',methods=["GET"])
def display():
    if request.method == "GET":
        month = request.args.get("total")
        a = request.args.get("t_prod")
        b = request.args.get("t_dept")
        return render_template("result.html",month = month,a=a,b=b)
    return f"POST method"

    
if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()