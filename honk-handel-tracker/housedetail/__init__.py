"""Housedetail ETL module"""

from typing import Optional

from .extract import Extract
from .transform import Transform
from .load import Load


def run_etl(extract: Optional[Extract], transform, load):
    """Run extract transform and load"""
    if extract:
        extract.execute()
    transformed_data = transform.execute()
    return load.execute(transformed_data)
