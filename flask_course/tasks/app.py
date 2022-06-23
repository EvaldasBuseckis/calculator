#Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus keliamuosius metus nuo 1900 iki 2100 metų.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def ar_keliamieji():
    for x in range (1900, 2100):
        if x % 400 == 0 or x % 100 != 0 and x % 4 == 0:
            return x
        else:
            return None

def home():
    vardai = ['Jonas', 'Antanas', 'Petras']
    return render_template("index.html", sarasas=ar_keliamieji)

if __name__ == "__main__":
    app.run()

