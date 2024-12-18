import requests
import apikey
import os

#mytoken USqEgyK9qP1NfshrPZGG

api_key = "USqEgyK9qP1NfshrPZGG"
url = 'https://the-one-api.dev/v2/character'
authorization_headers = {
	'Authorization: Bearer ' + the_one_api_key
}

response = requests.get(url, headers=authorization_headers)
print(response.status_code)

import os
the_one_api_key = os.environ['THE_ONE_API_KEY']
print(the_one_api_key)

import apikey

apikey.save("THE_ONE_API_KEY", "USqEgyK9qP1NfshrPZGG")

the_one_api_key = apikey.load("THE_ONE_API_KEY")