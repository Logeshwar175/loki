from flask import Flask, render_template
app = Flask(__name__)

@app.route("/student/<int:score>")
def student_name(score):
    return render_template("index.html", marks= score)




if __name__ == "__main__":
    app.run(debug=True)
    