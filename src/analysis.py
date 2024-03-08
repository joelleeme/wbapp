import pandas as pd
from models import db, RealEstate, CrimeRate

def perform_analysis():
    real_estate_data = pd.read_sql(RealEstate.query.statement, db.session.bind)
    crime_data = pd.read_sql(CrimeRate.query.statement, db.session.bind)
    correlation = real_estate_data['price'].corr(crime_data['crime_rate'])

    return {'correlation': correlation}