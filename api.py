from flask import Flask,render_template,url_for,redirect,request

app = Flask(__name__)


@app.route('/')                    
def home():
	return render_template('home.html',home="home")


@app.route('/about') 
def about():
	abcd="amazon big project"
	return render_template('about.html',h1=abcd)


@app.route('/contact')
def contact():
	return render_template('contact.html')


@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/layout')
def layout():
	return render_template('layout.html')

@app.route('/login',methods=['POST'])
def login():
	user={'username':'nikitha','password':'hello'}

@app.route('/title')
def title():
	a='this is amazing'
	return render_template('title.html',title=a)


	username= request.form['username']
	password= request.form['password']

	if user['username']==username:
		if user['password']==password:
			return redirect(url_for('welcome'))
		return "wrong password, go back and try again"
	return "this user doesnt exist,go back and enter a valid password"


if __name__=='__main__':

	app.run(debug=True)