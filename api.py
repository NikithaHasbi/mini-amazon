from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)


@app.route('/')                    
def home():
	return render_template('home.html',home="home")


@app.route('/about') 
def about():
	
	return render_template('about.html')


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login',methods=['POST'])
def login():
	user={'username':'nikitha','password':'hello'}

	username= request.form['username']
	password= request.form['password']

	if user['username']==username:
		if user['password']==password:
			return redirect(url_for('welcome'))
		return "wrong password, go back and try again"
	return "this user doesnt exist,go back and enter a valid password"


if __name__=='__main__':

	app.run(debug=True)