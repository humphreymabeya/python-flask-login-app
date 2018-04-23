# local imports
import os
from tabledefinition import *
from sqlalchemy.orm import sessionmaker
from flask import  Flask
from flask import Flask,flash,redirect, render_template, abort, request, session
app = Flask(__name__)

@app.route("/")
def home():
    if not session.get('logged in'):
        return render_template('login.html')
    else:
        return "hi, am your developer for today!! Logged in as %s <a href='/logout'>Logout</a>" 


@app.route('/login', methods = ['POST'])
def admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
    print(POST_USERNAME)
    print('===================')
    print(POST_PASSWORD)
    
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged in'] = True
    else:
        flash('wrong password!')
    return home()
@app.route("/logout")
def logout():
    session['logged in'] = False
    return home()

# app run
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
