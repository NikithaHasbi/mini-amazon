from pymongo import MongoClient
from bson.objectid import ObjectId

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

	# query = {'username':username}
	# result = db['users'].find_one(query)


	# if result['cart'].get(product_id):
	# 	db['users'].update({'username':username },{"$inc":{f"cart.{product_id}":1}})
	# 	return True
	# db['users'].update({'username':username },{"$set":{f"cart.{product_id}":1}})

	# # db.users.update( {'username':username},{ '$addToSet': { 'cart': { '$each': [ product_id ] } } })

	query = {'username':username}
	result = db['users'].find_one(query)


	if result['cart'].get(product_id):
		db['users'].update({'username':username },{"$inc":{f"cart.{product_id}":1}})
		return True
	db['users'].update({'username':username },{"$set":{f"cart.{product_id}":1}})
	# db.users.update( {'username':username},{ '$addToSet': { 'cart': { '$each': [ product_id ]} } })


	
def remove_prod_from_cart(product_id,username):

	query = {'username':username}
	result = db['users'].find_one(query)

	if result['cart'].get(product_id)<=1:
		db['users'].update({'username':username },{"$unset":{f"cart.{product_id}":1}})
		return True		
	db['users'].update({'username':username },{"$inc":{f"cart.{product_id}":-1}})
	
def cart_info(username):

	query = {'username':username}
	result = db['users'].find_one(query)['cart'].keys()

	products = []
	quantity = []
	for product_id in result:
		products.append( db['products'].find_one({'_id':ObjectId(product_id)}))
		quantity.append(db['users'].find_one({'username':username})['cart'][product_id])
					
	return products,quantity
 
def clear_cart(username):

 	db['users'].update({'username':username },{"$unset":{"cart":1}})
 	db['users'].update({'username':username },{"$set":{"cart":{}}})








 	








