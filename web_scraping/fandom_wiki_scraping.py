import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Collect category links
base_url = "https://harrypotter.fandom.com"
start_url = base_url + "/wiki/Category:Individuals_by_year_of_birth"

response = requests.get(start_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all category links
category_links = []
categories = soup.find_all('a', href=True, class_='category-page__member-link')
for category in categories:
    link = base_url + category['href']
    category_name = category.get_text()  # Get the category name (e.g., "20th century births")
    category_links.append((link, category_name))

# Step 2: Visit each link and collect character names with their year of birth
characters = []

for link, year in category_links:
    category_response = requests.get(link)
    if category_response.status_code == 200:
        category_soup = BeautifulSoup(category_response.text, "html.parser")
        character_tags = category_soup.find_all('a', href=True, class_='category-page__member-link')
        
        for character_tag in character_tags:
            character_name = character_tag.get_text()
            characters.append((character_name, year))
    else:
        print(f"Error: Could not retrieve the page {link}")

# Step 3: Save character names and their year of birth to a CSV file in table format
with open('harry_potter_characters.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Character Name', 'Year of Birth'])
    for character, year in characters:
        writer.writerow([character, year])

print("Character names and years of birth successfully saved to harry_potter_characters.csv")
