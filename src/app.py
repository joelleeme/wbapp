from flask import Flask, jsonify, request, render_template
import pandas as pd
from sodapy import Socrata

app = Flask(__name__)

APP_TOKEN = "Ebee12uwTIwfavknSTKzrL7jK"
REAL_ESTATE_DATASET_IDENTIFIER = "5mzw-sjtu"
SOCRATA_DOMAIN = "data.ct.gov"

def fetch_real_estate_data(limit=100):
    client = Socrata(SOCRATA_DOMAIN, APP_TOKEN)
    results = client.get(REAL_ESTATE_DATASET_IDENTIFIER, limit=limit)
    return results

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/real-estate/analysis', methods=['GET'])
def real_estate_analysis():
    start_year = request.args.get('startYear', type=int, default=2001)
    end_year = request.args.get('endYear', type=int, default=2021)

    data = fetch_real_estate_data(limit=5000)
    df = pd.DataFrame.from_records(data)

    df['saleamount'] = pd.to_numeric(df['saleamount'].str.replace('$', '', regex=False).replace(',', '', regex=False), errors='coerce')
    df['daterecorded'] = pd.to_datetime(df['daterecorded'])
    df['year'] = df['daterecorded'].dt.year

    filtered_df = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    average_prices_per_year = filtered_df.groupby('year')['saleamount'].mean().reset_index()

    analysis_result = average_prices_per_year.to_dict(orient='records')

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)