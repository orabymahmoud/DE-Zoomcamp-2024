import io
import pandas as pd
import requests
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.postgres import Postgres
from os import path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """

    for data in ['yellow' , 'green']:
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{data}/{data}_tripdata_2019-01.csv.gz'

        df_iter = pd.read_csv(url , iterator = True , chunksize = 100000 ,compression ='gzip')
        schema_name = 'trips_data_all'  # Specify the name of the schema to export data to
        table_name = f'{data}_tripdata_2019_01'  # Specify the name of the table to export data to
        config_path = path.join(get_repo_path(), 'io_config.yaml')
        config_profile = 'default'  

        for i , chunk in enumerate(df_iter):
            with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
                loader.export(
                    chunk,
                    schema_name,
                    table_name,
                    index=False,  # Specifies whether to include index in exported table
                    if_exists='append',  # Specify resolution policy if table name already exists
                )
            print(f"{table_name}: Chunk {i} loaded successfully ")
        print(f"{table_name}: loaded fully successfully ")

