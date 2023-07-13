"""Housedetail ETL module"""
from .extract import Extract
from .transform import Transform
from .load import Load


def run_etl(extract, transform, load):
    """Run extract transform and load"""
    # extract.execute()
    transformed_data = transform.execute()
    return load.execute(transformed_data)
