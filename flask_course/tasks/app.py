#Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.

from flask import Flask, render_template

app = Flask(__name__)



def get_leap_year() -> list:
    list1 = []
    for x in range(1900, 2100):
        if x % 400 == 0 or x % 100 != 0 and x % 4 == 0:
            list1.append(x)
    return  list1

@app.route("/")
def home():
    leap_years = get_leap_year()
    return render_template("index.html", sarasas=leap_years)

if __name__ == "__main__":
    app.run()

