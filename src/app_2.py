import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ckan_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class CKANData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)

def fetch_ckan_data(resource_id='595b402d-4192-401c-b740-5cb7e4ceab10', limit=5, query=None):
    base_url = 'http://data.ctdata.org/api/action/datastore_search'
    params = {'resource_id': resource_id, 'limit': limit}
    if query:
        params['q'] = query
    
    try:
        response = requests.get(base_url, params=params)
        logging.info(f"Request URL: {response.request.url}")
        response.raise_for_status()
        
        data = response.json()
        logging.info(f"Response Data: {data}")
        
        if data and 'result' in data and 'records' in data['result']:
            return data['result']['records']
        else:
            logging.warning("Expected data not found in response")
            return []
    except requests.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err} - Status code: {response.status_code}")
    except Exception as err:
        logging.error(f"An unexpected error occurred: {err}")
    return []

@app.cli.command('fetch-store')
def fetch_store():
    records = fetch_ckan_data(limit=5, query=None)
    if records:
        for record in records:
            data_entry = CKANData(data=str(record))
            db.session.add(data_entry)
        db.session.commit()
        print(f"Data fetched and stored successfully. {len(records)} records added.")
    else:
        print("No data was fetched (Please check your query)")

@app.route('/')
def home():
    """FOR TEST: Home route to display a message."""
    return "Use the CLI command 'flask fetch-store' to fetch and store data."

if __name__ == "__main__":
    app.run(debug=True)