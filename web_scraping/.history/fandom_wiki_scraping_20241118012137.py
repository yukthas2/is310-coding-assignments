from bs4 import BeautifulSoup
import requests
import csv

# Fandom of Choice: Harry Potter
url = "https://harrypotter.fandom.com/wiki/Category:Characters"
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all character links on the page
    characters = soup.find_all('a', class_='category-page__member-link')
    
    # Create and write to the CSV file
    with open('/Users/yukthasureshkumar/Desktop/is310-coding-assignments/web_scraping/harry_potter_characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Link'])  # Header row
        
        # Iterate through each character link found
        for character in characters:
            character_name = character.get_text()  # Get the text (character name)
            character_link = "https://harrypotter.fandom.com" + character.get('href')  # Get the full link
            writer.writerow([character_name, character_link])  # Write to CSV

    print("Character names saved successfully! Data saved to harry_potter_characters.csv.")
else:
    print("Error: Could not retrieve the page.")
