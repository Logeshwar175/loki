from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello/<int:score>")
def hello_name(Score):
    return render_template("index.html",mark= Score)

if __name__=="__main__":
    app.run(debug=True)