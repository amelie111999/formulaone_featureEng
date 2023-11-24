# content of test_sample.py

import pandas as pd
from load_movie_data.helpers import get_dyname_recouce

def test_check_item():
    dynamo = get_dyname_recouce()
    tables = []
    for table in dynamo.tables.all():
        tables.append(table.name)

    assert 'doc-example-table-movies' in tables