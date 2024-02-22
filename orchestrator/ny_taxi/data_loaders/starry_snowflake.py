import io
import pandas as pd
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Provide the URL of the Google Sheets file
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ2T5mAu0AInrXGltn8nTgYjLYyDyGEmMsLHJQZg9kWQjl-5behuJ4sKow-iq7L-_U82kC3io4XDIro/pub?gid=0&single=true&output=csv'

    # Use pandas to read the Google Sheets file directly
    df = pd.read_csv(url)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
