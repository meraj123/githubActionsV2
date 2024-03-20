import requests
import os

def run_databricks_notebook():
    databricks_host = os.environ.get('https://dbc-0b374bc7-abe1.cloud.databricks.com/')
    databricks_token = os.environ.get('dapif65430eaaec148a8979e16bda73eefc9')
    notebook_path = os.environ.get('/Users/merajalam@in.bosch.com/Notebook-V1')

    headers = {
        'Authorization': f'Bearer {databricks_token}',
        'Content-Type': 'application/json'
    }

    data = {
        'path': notebook_path
    }

    response = requests.post(f'https://{databricks_host}/api/2.0/jobs/run-now', headers=headers, json=data)

    if response.status_code == 200:
        print('Databricks notebook run successfully triggered.')
    else:
        print(f'Error: {response.status_code} - {response.text}')

if __name__ == '__main__':
    run_databricks_notebook()
