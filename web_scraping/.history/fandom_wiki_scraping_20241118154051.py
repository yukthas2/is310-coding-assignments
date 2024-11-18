import requests
from bs4 import BeautifulSoup
import csv
import re
from rich.console import Console
from rich.table import Table

# Initialize console for Rich output
console = Console()

# Function to get the language translations for a character page
def get_character_languages(url):
    response = requests.get(url)
    if response.status_code != 200:
        console.print(f"Error: Could not retrieve the page {url}", style="red")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    # Using regex to find translation links
    languages = soup.find_all('a', attrs={'data-tracking-label': re.compile(r'lang-')})
    return [{"language": language.get('data-tracking-label'), "language_name": language.get_text()} for language in languages]

# Function to fetch character information from a category URL
def fetch_characters(url, category):
    response = requests.get(url)
    if response.status_code != 200:
        console.print(f"Error: Could not retrieve the page {url}. Status code: {response.status_code}", style="red")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    characters = soup.find_all('a', class_='category-page__member-link')
    characters_data = []

    for character in characters:
        console.print(f"Processing {character.get_text()}...", style="green")
        character_data = {
            "character": character.get_text(),
            "character_link": "https://harrypotter.fandom.com/wiki/Category:Deceased_individuals" + character.get('href'),
            "category": category
        }
        character_data['languages'] = get_character_languages(character_data['character_link'])
        character_data['languages_count'] = len(character_data['languages'])
        characters_data.append(character_data)
    
    return characters_data

# URLs for Harry Potter character categories (you may need to update these if necessary)
canon_characters_url = "https://harrypotter.fandom.com/wiki/Category:Deceased_individuals"
# You can add more URLs if you have different categories to scrape

# Fetch characters from the given URLs
canon_characters_data = fetch_characters(canon_characters_url, "Canon")

# Sort characters by language count
sorted_characters = sorted(canon_characters_data, key=lambda x: x['languages_count'], reverse=True)

# Display the sorted characters in a table
table = Table(title="Harry Potter Characters and Their Translations")
table.add_column("Character", style="cyan")
table.add_column("Language Count", style="magenta")
table.add_column("Category", style="green")

for character in sorted_characters:
    table.add_row(character['character'], str(character['languages_count']), character['category'])

console.print(table)

# Save data to a CSV file
with open('harry_potter_characters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Character', 'Character Link', 'Languages', 'Languages Count', 'Category'])
    for character in sorted_characters:
        writer.writerow([character['character'], character['character_link'], character['languages'], character['languages_count']])

console.print("Data saved to harry_potter_characters.csv", style="blue")
