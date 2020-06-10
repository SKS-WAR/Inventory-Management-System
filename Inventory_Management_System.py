from flask import Flask,redirect,url_for, render_template, request
try:
    import sendDataToFirebase
except :
    pass
import webbrowser
import desktopNotification
app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        dt = request.form["date"]
        product_name = request.form["product"]
        units = request.form["units"]
        price = request.form["price"]
        #sending data to firebase
        try:
            sendDataToFirebase.sendData(name=product_name,price=price,quantity=units)
            desktopNotification.notify("Data Inserted successfully")
        except :
            desktopNotification.notify("Some Issues Arised")
        return redirect(url_for("home"))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000')
    app.run()