from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age():

    result = ""

    if request.method == "POST":

        birth_year = int(
            request.form["birth_year"]
        )

        current_year = datetime.now().year

        result = current_year - birth_year

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
