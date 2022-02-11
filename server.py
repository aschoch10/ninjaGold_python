import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super, super secret key name'


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
