"""Housedetail ETL module"""
from .extract import Extract
from .transform import Transform
from .load import Load


def run_etl(extract, transform, load):
    """Run extract transform and load"""
    extracted_data = extract.execute()
    transformed_data = transform.execute(extracted_data)
    loaded_data = load.execute(transformed_data)
    print(loaded_data)
