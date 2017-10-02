from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hey():
    return render_template('form.html')

@app.route("/yay", methods=["POST"])
def ya():
    r = request.form #dictionary
    r2 = request.method
    return render_template("seed.html", username=r["username"], method=r2)

if __name__ == "__main__":
    app.debug = True
    app.run()
