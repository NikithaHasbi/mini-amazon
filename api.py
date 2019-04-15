from flask import Flask,render_template,url_for,redirect,request,session
from models.model import user_exists,create_user,login_user,product_exists,add_prod,find_products,add_product_to_cart,remove_prod_from_cart,cart_info,clear_cart
from flask_mail import Mail, Message
import os

app = Flask(__name__)

mail = Mail(app)
app.config['SECRET_KEY']= 'helllo'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get('DB_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('DB_PASS')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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

@app.route('/add_products',methods=["POST","GET"])
def add_products():

	if request.method=='POST' :

		seller={}

		seller['pname']= request.form['pname']
		seller['sname']=session['username']
		seller['price']=int (request.form['price'])
		seller['description']=request.form['description']

		if product_exists(seller['pname']) is False:
			add_prod(seller)
			return render_template('home.html')
		return "product already exists"

	else:

		return redirect(url_for('home'))

@app.route('/products_page')
def products_page():

	return render_template('products.html',products=find_products(session))
	
@app.route('/add_cart', methods=['POST'])
def add_cart():

	product_id=str(request.form['pid'])
	add_product_to_cart(product_id,session['username'])
	return redirect(url_for('cart'))

@app.route('/remove_cart', methods=['POST'])
def remove_cart():

	product_id= str(request.form['pid'])
	remove_prod_from_cart(product_id,session['username'])
	return redirect(url_for('cart'))


@app.route('/cart', methods=['POST','GET'])
def cart():

	temp=cart_info(session['username'])
	product_info= temp[0]
	quantity= temp[1]

	total= 0

	for product, quant in zip(product_info,quantity):
		total = total + (product['price'] * quant)
		session['cart_total']= total
	return render_template('cart.html',cart=zip(product_info,quantity), total= session['cart_total'])


@app.route('/buy', methods=['POST','GET'])
def buy():

	msg = Message('Hello', sender = os.environ.get('DB_USER'), recipients = ['nikithahasbi07@gmail.com'])
	msg.body = f"Hello {session['username']},Flask message sent from Flask-Mail"
	mail.send(msg)
	clear_cart(session['username'])
	return redirect(url_for('home'))


@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))


if __name__=='__main__':

	app.run(debug=True)