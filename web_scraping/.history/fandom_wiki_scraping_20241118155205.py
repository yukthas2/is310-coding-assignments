import requests
from bs4 import BeautifulSoup
import csv

# Function to fetch characters from the given URL
def fetch_characters(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Could not retrieve the page {url}. Status code: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    characters = soup.find_all('a', class_='category-page__member-link')
    character_data = []

    for character in characters:
        name = character.get_text()
        link = "https://harrypotter.fandom.com" + character.get('href')
        character_data.append([name, link])

    return character_data

# URL of the page to scrape
url = "https://harrypotter.fandom.com/wiki/Category:Deceased_individuals"
characters = fetch_characters(url)

# Save the character names and links to a CSV file
with open('harry_potter_characters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Character', 'Link'])
    writer.writerows(characters)

print("Data saved to harry_potter_characters.csv")

