from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Database Setup
#################################################
engine = create_engine("sqlite:////Users/sarakleine-kracht/Desktop/group-3-proj-3/nash_restaurants.sqlite")

# # reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
restaurants = Base.classes.restaurant_info
categories = Base.classes.restaurant_categories

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Define what to do when a user hits the /jsonified route
@app.route("/jsonified")
def jsonified():
    session=Session(engine)

    joined_tables = session.query(restaurants, categories).join(categories, restaurants.name == categories.name).all()

    session.close()

    # Assuming you want to convert the result into a dictionary for JSON serialization
    table_dict = []
    for restaurant, category in joined_tables:
        data_dict = {}
        data_dict['Restaurant Name'] = restaurant.name,
        data_dict['Restaurant Rating'] = restaurant.rating, 
        data_dict['Restaurant Pricing'] = restaurant.pricing,
        data_dict['Number of Reviews'] = restaurant.number_of_reviews,
        data_dict['Restaurant Location'] = restaurant.location,  
        data_dict['Restaurant Category'] = category.category,
        table_dict.append(data_dict)

        
    return jsonify(table_dict)

if __name__ == "__main__":
    app.run(debug=True)