from flask import Flask,render_template,url_for,redirect,request,session
from models.model import user_exists,create_user,login_user

app = Flask(__name__)
app.config['SECRET_KEY']= 'helllo'


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




@app.route('/title')
def title():
	a='this is amazing'
	return render_template('title.html',title=a)


@app.route('/login',methods=['POST','GET'])
def login():
	if request.method == 'POST':

		username= request.form['username']
		password= request.form['password']


		user= login_user(username)

		if user is None:
			return "this user doesnt exist. go back and enter a valid user"

		if user['username']==username:
			if user['password']==password:
				session['username']= user['username']
				session['c_type']=user['c_type']
				return redirect(url_for('home'))
			return "wrong password, go back and try again"
		return "this user doesnt exist,go back and enter a valid password"
	else:
		return redirect(url_for('home'))

@app.route('/signup',methods=['POST','GET'])
def signup():

	if request.method == 'POST':

		user_info={}

		user_info['username']= request.form['username']
		user_info['email']= request.form['email']
		user_info['password']=request.form['password']
		user_info['c_type']=request.form['c_type']
		rpassword = request.form['rpassword']

		if user_exists(user_info['username']) is False:
			if user_info['password'] == rpassword:
				if user_info['c_type']== 'buyer':
					user_info['cart']=[]
				create_user(user_info)
				return render_template('welcome.html', user= user_info['username'])
			return "passwords dont match please re enter the password"
		return "user already exists. Enter another username"
	else: 
		return redirect(url_for('home'))

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))


if __name__=='__main__':

	app.run(debug=True)