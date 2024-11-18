import requests
from bs4 import BeautifulSoup
import csv
import json

# Open the CSV file
with open('/Users/yukthasureshkumar/Desktop/is310-coding-assignments/web_scraping/harry_potter_characters.csv', mode='r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

scraped_data = []

for item in data:
    name = item['name']
    link = item['link']

    # Fetch the page
    response = requests.get(link)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Scrape the first paragraph of the page
        description = soup.find('p').text if soup.find('p') else 'No description available'
        
        scraped_data.append({
            'name': name,
            'description': description
        })
    else:
        print(f"Failed to retrieve data for {name}")

# Save the data to a JSON file
with open('web_scraping_assignments/scraped_data.json', mode='w') as json_file:
    json.dump(scraped_data, json_file, indent=4)

print("Scraping complete. Data saved to scraped_data.json.")

