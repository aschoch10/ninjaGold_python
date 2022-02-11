import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'super, super secret key name'


@app.route('/')
def home():
        return render_template("index.html")

@app.route('/submit' , methods=['POST'])
def render():
    if 'gold' not in session:
        session['gold'] = 0
        # session['activities'] = []
    
    if request.form['findGold']=='cave':
        session['gold'] += random.randint(5,10)
        return redirect("/")
    
    elif request.form['findGold']=='farm':
        session['gold'] += random.randint(10,20)
        return redirect("/")
    elif request.form['findGold']=='house':
        session['gold'] += random.randint(2,5)
        return redirect("/")
    elif request.form['findGold']=='casino':
        session['gold'] += random.randint(-50,50)
        return redirect("/")
    

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
