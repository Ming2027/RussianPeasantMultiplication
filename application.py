from flask import Flask, redirect, render_template, request
from bernstein_vazirani import quantum_calculate

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/compute", methods=["POST"])
def compute():
    c = 0
    a = int(request.form.get("a"))
    b = int(request.form.get("b"))
    a_str = quantum_calculate(a)
    b_str = quantum_calculate(b)
    a_n = len(a_str)
    x = []
    c = 0
    for i in range(a_n):
        j = a_n - i - 1
        x.append([a_str[j], (b_str + ('0'*i))])

    for item in x:
        if item[0] == '1':
            d = item[1]
            e = int(d, 2)
            c += e
    data = {"a":a, "b":b, "c":c}
    return render_template("answer.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)