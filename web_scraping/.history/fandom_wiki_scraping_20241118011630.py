import requests
from bs4 import BeautifulSoup
import csv  

response = requests.get("https://harrypotter.fandom.com/wiki/Category:Characters")


soup = BeautifulSoup(response.text, "html.parser")

# Find character elements
characters = soup.find_all('a', class_='category-page__member-link')


characters_data = []

for character in characters:
    character_name = character.get_text()
    character_link = "https://harrypotter.fandom.com" + character.get('href')
    characters_data.append({"name": character_name, "link": character_link})

# Save data to a CSV file
with open("harry_potter_characters.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "link"])
    writer.writeheader()
    writer.writerows(characters_data)

print("Data has been saved to harry_potter_characters.csv")
