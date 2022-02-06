
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    text = open('xd.txt').read()
    return render_template("index.html", text=text)

@app.route('/xd')
def xd():
    text = open('flaga_xd.txt').read()
    return render_template("xd.html", text=text)
<<<<<<< HEAD
    
=======


>>>>>>> create xd page

if __name__=="__main__":
    app.run()
