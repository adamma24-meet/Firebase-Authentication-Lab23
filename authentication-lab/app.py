from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase




firebaseConfig = {
  "apiKey": "AIzaSyCfYqzCgmLLNa0dhWf-BKu0sW25L9vK37I",
  "authDomain": "adammm-95a11.firebaseapp.com",
  "projectId": "adammm-95a11",
  "storageBucket": "adammm-95a11.appspot.com",
  "messagingSenderId": "509557476876",
  "appId": "1:509557476876:web:c4dd591c0f61d39768a829",
  "measurementId": "G-H1KE36PRQ8",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')




app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']

       try:
        login_session['user'] = auth.sign_in_with_email_and_password(email, password)
        return return_template("add_tweet.html")
       except:
        error = "Authentication failed"
        return render_template("signin.html")
    else:
        return render_template("signin.html")


   

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = ""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] =  auth.create_user_with_email_and_password(email, password)
            return render_template("add_tweet.html")
        except:
            error = "Authentication failed"
            return render_template("signup.html")
    else:
        return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)