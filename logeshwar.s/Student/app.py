from flask import Flask,render_template, url_for,request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template("index.html")

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method =='POST':
        result=request.form
        return render_template('result.html',result=result)

if __name__ == "__main__":
    app.run(debug=True)
    