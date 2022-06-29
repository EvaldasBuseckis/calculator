from flask import Flask, request, render_template
app = Flask(__name__)

def ar_keliamieji(x:int) -> bool:
    if x % 400 == 0 or x % 100 != 0 and x % 4 == 0:
        return True
    else:
        return False

@app.route("/leap", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        year = int(request.form['year'])
        result = ar_keliamieji(year)

        if result is True:
            result = "This is a leap year!!"
        else:
            result = "This is not a leap year!!"

        return render_template("leapresult.html", result=result)
    else:
        return render_template("leap.html")


if __name__ == "__main__":
    app.run()