from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()

line = "Trust your toungue more than our words! So taste the first one for free!"

restaurant1 = Restaurant(name="Burger King")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Veggie Burger", price="$2.99", description=line, restaurant=restaurant1)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Eggie Burger", price="$3.99", description=line, restaurant=restaurant1)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chicken Burger", price="$4.99", description=line, restaurant=restaurant1)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Beef Burger", price="$5.99", description=line, restaurant=restaurant1)
session.add(menuItem4)
session.commit()

#####################################################################################

restaurant2 = Restaurant(name="Pizza Hut")
session.add(restaurant2)
session.commit()

menuItem1 = MenuItem(name="Veggie Pizza", price="$2.99", description=line, restaurant=restaurant2)
session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Eggie Pizza", price="$3.99", description=line, restaurant=restaurant2)
session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Chicken Pizza", price="$4.99", description=line, restaurant=restaurant2)
session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(name="Beef Pizza", price="$5.99", description=line, restaurant=restaurant2)
session.add(menuItem4)
session.commit()

print "added menu!"