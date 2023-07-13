"""Housedetail ETL module"""
from .extract import Extract


def run_etl(extract):
    """Run extract transform and load"""
    extracted_data = extract.execute()
    print(extracted_data)
