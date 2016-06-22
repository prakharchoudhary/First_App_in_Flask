from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.binkd = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
def HomePage():
	restaurant = session.query(Restaurant).all()
	return render_template('homepage.html',restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/')		#lets us use a variable in the path name
def restaurantMenu(restaurant_id):
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
	output = render_template('menu.html', restaurant= restaurant, items = items)

	return output

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
	if request.method == 'POST':
		newItem = MenuItem(name=request.form['name'], restaurant_id = restaurant_id)
		session.add(newItem)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id= restaurant_id))
	else:
		return render_template('new.html', restaurant_id=restaurant_id)
	

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id,menu_id):
	itemToEdit = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		itemToEdit.name = request.form['name']
		itemToEdit.price = request.form['price']
		itemToEdit.description = request.form['description']
		session.add(itemToEdit)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id= restaurant_id))
	else:
		return render_template('edit.html', restaurant_id=restaurant_id, menu_id=menu_id, item=itemToEdit)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
	itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
	if request.method == 'POST':
		session.delete(itemToDelete)
		session.commit()
		return redirect(url_for('restaurantMenu', restaurant_id= restaurant_id))
	else:
		return render_template('delete.html', restaurant_id=restaurant_id, menu_id=menu_id, item=itemToDelete)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)