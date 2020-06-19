from flask import Flask,redirect,url_for, render_template, request,send_file,session
try:
    import sendDataToFirebase
except :
    pass
import webbrowser
import desktopNotification
import firebase

app = Flask(__name__)
app.secret_key = "BIGsecretOfMine&plzDontDecrptMe"

@app.route("/",methods=["POST","GET"])
@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form["uname"]
        password = request.form["password"]
        user = firebase.login(name,password)
        session['user'] = user
        if user != None :
            return redirect(url_for("product"))
        else:
            return render_template('login.html')
    else:
        return render_template("login.html")

@app.route("/product",methods=["POST","GET"])
def product():
    if 'user' in session:
        user = session["user"]
        if request.method == "POST":
            dt = request.form["date"]
            product_name = request.form["product"]
            units = request.form["units"]
            price = request.form["price"]
            #sending data to firebase
            try:
                sendDataToFirebase.sendProductionData(name=product_name,date=dt,price=price,quantity=units)
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
            d = request.form["date"]
            p_name = request.form["product"]
            unts = request.form["units"]
            amount = request.form["price"]
            #sending data to firebase
            try:
                sendDataToFirebase.sendDespatchData(name=p_name,date=d,price=amount,quantity=unts)
                desktopNotification.notify("Data Inserted successfully")
            except :
                desktopNotification.notify("Some Issues Arised")
            return redirect(url_for("despatch"))
        else:
            return render_template("despatch.html")
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

@app.route('/query',methods=["GET","POST"])
def query():
    if request.method == "POST":
        user = request.form["name"]
        password = request.form["pass"]
        return redirect(url_for("display",usr=user,psw=password))
    else:
        return render_template("New.html")
        
@app.route('/result',methods=["GET"])
def display():
    if request.method == "GET":
        user = request.args.get("usr")
        password = request.args.get("psw")
    return f"<h1>The user is {user} and password is {password}"


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    app.run()