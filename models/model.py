from pymongo import MongoClient

client = MongoClient()
db = client['amazon']

def user_exists(username):

	query = {'username':username}
	result =  db['users'].find(query)

	if result.count()>0:
		return True
	return False 



def create_user(user_info):
	db['users'].insert_one(user_info)


def login_user(username):

	query = {'username':username}
	result =  db['users'].find_one(query)

	return result

def product_exists(pname):

	query={'product name': pname}
	result = db['products'].find(query)

	if result.count()>0:
		return True
	return False

def add_prod(seller):
	db['products'].insert_one(seller)


# def buyer_products():
# 	result=db['products'].find({})
# 	return result

# def seller_products(username):

# 	result=db['products'].find({'sname':sname})
# 	return result

def find_products(session):
	if session['c_type']== 'buyer':
		result=db['products'].find({})
		return result
	result=db['products'].find({'sname': session['username']})
	return result

def add_product_to_cart(product_id,username):
	db.users.update( {'username':username},{ '$addToSet': { 'cart': { '$each': [ product_id ] } } })
	






