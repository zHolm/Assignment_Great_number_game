from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key ="''asd';b;jjflkhvkhh346878g'"


@app.route("/")
def rando():
    session['num'] = random.randint(1,100)
    print(session['num'])
    session['guess'] = None
    

    return render_template("index.html")

@app.route('/', methods=['POST'])         
def guess():
    print(f"my number is {session['num']}")
    
    guess= request.form['guess']
    session['guess']=int(guess)
  

    if 'guess_arr' in session:
        temp_list = session['guess_arr']
        temp_list.append(session['guess'])
        session['guess_arr'] = temp_list
        print('key exists')
    else:
        session['guess_arr'] = [session['guess']]
        print('key doesnt exist')

    session['number_of_guesses'] = int(len( session['guess_arr']))
    
  
   
    print(f"your guess is {guess}")
    print(session['guess_arr'])
    
   
    return redirect("/guess")

@app.route("/guess")
def make_guess():
    return render_template("index.html", num = session['num'], guess=session['guess'], number_of_guesses=session['number_of_guesses'])

@app.route("/destroy_session")
def reset():
    session.clear()		# clears all keys
    session.pop('guess_arr', None)
    return redirect("/")	

if __name__=="__main__":
    app.run(debug=True)