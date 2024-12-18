import requests
import pandas as pd
import apikey
import os
import pyeuropeana.apis as apis
import pyeuropeana.utils as utils


#eurokey: ullickyapoen
#mytoken USqEgyK9qP1NfshrPZGG


url = "https://swapi.py4e.com/api/people/?search=Luke Skywalker"  # Search for Luke Skywalker
response = requests.get(url)


if response.status_code == 200:
    swapi_data = response.json()
    print("SWAPI Response:", swapi_data)
else:
    print("Error fetching data from SWAPI:", response.status_code)


luke_data = swapi_data['results'][0]
name = luke_data['name']
birth_year = luke_data['birth_year']
films = luke_data['films']  

print(f"Name: {name}, Birth Year: {birth_year}, Films: {films}")

apikey.save("EUROPEANA_API_KEY", "ullickyapoen")
europeana_api_key = apikey.load("EUROPEANA_API_KEY")

os.environ['EUROPEANA_API_KEY'] = europeana_api_key

europeana_response = apis.search(query="Star Wars", rows=5)

if europeana_response['success']:
    europeana_df = utils.search2df(europeana_response)
    print("Europeana Results:\n", europeana_df)
else:
    print("Error fetching data from Europeana API")


combined_data = {
    "SWAPI": {
        "name": name,
        "birth_year": birth_year,
        "films": films
    },
    "Europeana": europeana_df.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
}


import json
with open("swapi_europeana_data.json", "w") as file:
    json.dump(combined_data, file, indent=4)

print("Data saved to swapi_europeana_data.json")

