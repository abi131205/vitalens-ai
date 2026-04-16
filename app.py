from flask import Flask, render_template, request
from logic import analyze_health

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        symptoms = request.form.get("symptoms")
        sleep = request.form.get("sleep")
        steps = request.form.get("steps")
        stress = request.form.get("stress")

        result = analyze_health(symptoms, sleep, steps, stress)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)