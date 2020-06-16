from flask import Flask,redirect,url_for, render_template, request,send_file
try:
    import sendDataToFirebase
except :
    pass
import webbrowser
import desktopNotification
app = Flask(__name__)

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        name = request.form["uname"]
        password = request.form["password"]
        return redirect(url_for("home"))
    else:
        return render_template("login.html")

@app.route("/",methods=["POST","GET"])
def home():
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
        return redirect(url_for("home"))
    else:
        return render_template("index.html")

@app.route("/despatch",methods=["POST","GET"])
def despatch():
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

#to download a file use <a href = "{{url_for('download_report')}}">Download</a>
@app.route("/download")
def download():
    return render_template("downlaod.html")
	
@app.route("/xyz")
def download_report():
    path = "robots.txt"
    return send_file(path,as_attachment=True)

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000')
    app.run()