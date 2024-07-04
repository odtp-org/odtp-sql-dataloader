#!/bin/python 

# Code originally developed by Ye Hong: https://github.com/irmlma/mobility-simulation

import sqlalchemy
from sqlalchemy import text
import pandas as pd
import os

# Variables
protocol = os.environ["PROTOCOL"]
login_user = os.environ["LOGIN_USER"]
password = os.environ["PASSWORD"]
host = os.environ["HOST"]
port = os.environ["PORT"]
database = os.environ["DATABASE"]
query = os.environ["QUERY"]
output_filename = os.environ["OUTPUT_FILENAME"] 

# Query
engine = sqlalchemy.create_engine(
    f"{protocol}://{login_user}:{password}@{host}:{port}/{database}"
)

# Remove the double quotes if they exist
if query.startswith('"') and query.endswith('"'):
    query = query[1:-1]

print(f'CONNECTING HOST: {host}:{port}/{database}')
with engine.connect() as conn:
    print(f'QUERY: {query}')
    df = pd.read_sql(text(query), conn)

engine.dispose()

# Storing CSV
output_filename = os.path.join("/odtp/odtp-output/", os.environ["OUTPUT_FILENAME"])
print(f'EXPORTING TO: {output_filename}')
df.to_csv(output_filename, index=False)