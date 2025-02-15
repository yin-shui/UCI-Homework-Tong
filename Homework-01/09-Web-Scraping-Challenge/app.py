from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo

import scrape_mars

# Create an instance of our Flask app
app = Flask(__name__)

# Using the flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mars_app'
mongo = PyMongo(app)




@app.route('/')
def index():
    # store collection in a list
    mars_dict = mongo.db.mars_dict.find_one()
    return render_template('index.html', mars_dict=mars_dict)


@app.route('/scrape')
def scraper():
    mars_dict = mongo.db.mars_dict
    mars_data = scrape_mars.scrape_mars()
    mars_dict.update({}, mars_data, upsert=True)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)