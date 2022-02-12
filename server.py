import random
from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'super, super secret key name'


@app.route('/')
def home():
        return render_template("index.html")

@app.route('/submit' , methods=['POST'])
def render():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    
    if request.form['findGold']=='cave':
        session['message'] = ''
        randoNum = random.randint(5,10)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += randoNum
        session['activities'].append(f"<div class='won'>Earned {randoNum} gold from the farm! ({time})</div>")
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]

    elif request.form['findGold']=='farm':
        session['message'] = ''
        randoNum = random.randint(10,20)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += randoNum
        session['activities'].append(f"<div class='won'>Earned {randoNum} gold from the farm! ({time})</div>")
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]
    
    elif request.form['findGold']=='house':
        session['message'] = ''
        randoNum = random.randint(2,5)
        time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += randoNum
        session['activities'].append(f"<div class='won'>Earned {randoNum} gold from the farm! ({time})</div>")
        for i in range(len(session['activities'])-1, -1, -1):
            session['message'] += session['activities'][i]
    
    elif request.form['findGold']=='casino':
        if session['gold'] > 0:
            session['message'] = ''
            randoNum = random.randint(-50,50)
            time = datetime.now().strftime("%Y/%m/%d %I:%M %p")
            session['gold'] += randoNum
            if randoNum > 0:
                print(f"Gold increased by {randoNum}.")
                session['activities'].append(f"<div class='won'>Earned {randoNum} gold from the casino! ({time})</div>")
            if randoNum < 0:
                print(f"Gold decreased by {abs(randoNum)}.")
                session['activities'].append(f"<div class='lost'>Entered a casino and lost {abs(randoNum)} gold....oof! ({time})</div>")
            print(f"Total Gold = {session['gold']}")
            for i in range(len(session['activities'])-1, -1, -1):
                session['message'] += session['activities'][i]

        elif session['gold'] <= 0:
            session['message'] = ''
            session['activities'].append(f"<div>You have no gold to gamble. Please come back to the casino when you have more money.</div>")
            # print(f"Total Gold = {session['gold']}")
            # print("You have no gold to gamble. Please come back to the casino when you have more money.")

            for i in range(len(session['activities'])-1, -1, -1):
                session['message'] += session['activities'][i]
    return redirect("/")
    

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
