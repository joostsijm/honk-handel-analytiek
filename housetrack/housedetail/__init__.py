"""Housedetail ETL module"""
from .extract import Extract
from .transform import Transform


def run_etl(extract, transform):
    """Run extract transform and load"""
    extracted_data = extract.execute()
    transformed_data = transform.execute(extracted_data)
    print(transformed_data.registration_date)
