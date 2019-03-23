from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home1.html')

	username= request.form['username']
	password= request.form['password']

		if user['username']==username:
			if user['password']==password:
				return "welcome to the page"
			return "password incoreect plz try again"
		return "this user doesn't exist"
		

if __name__ == '__main__':
	app.run(debug=True)
	