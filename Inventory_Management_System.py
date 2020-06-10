from flask import Flask,redirect,url_for, render_template, request
import sendDataToFirebase

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        dt = request.form["date"]
        print("Date:",(dt))
        product = request.form["product"]
        print("Product:",(product))
        units = request.form["units"]
        print("Number of units:",(units))
        price = request.form["price"]
        print("Price: Rs.",(price))
        #sending data to firebase
        sendDataToFirebase.sendData(name=product,desc="",price=price,quantity=units)        
        return redirect(url_for("home"))
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()