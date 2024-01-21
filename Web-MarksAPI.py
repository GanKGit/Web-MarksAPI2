from flask import Flask, render_template

app = Flask("Website")

@app.route("/")
def home():
    return render_template("home.html")


marks_list = {
    "100": {"Maths": 98, "Science": 96, "English": 89},
    "101": {"Maths": 89, "Science": 97, "English": 82},
    "102": {"Maths": 92, "Science": 96, "English": 81},
    "103": {"Maths": 86, "Science": 93, "English": 99},
    "104": {"Maths": 90, "Science": 99, "English": 80}
}

# Lookup function
def lookup(SSNo):
    return marks_list[SSNo]

@app.route("/v1/<ssno>/")
def look(ssno):
    marks=lookup(ssno)
    marks['SSNo']=ssno
    return marks

app.run(debug=True, port=5000)