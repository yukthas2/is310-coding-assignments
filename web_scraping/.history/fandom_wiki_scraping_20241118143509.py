from bs4 import BeautifulSoup
import requests
import csv

# Fandom of Choice: Harry Potter
url = "https://harrypotter.fandom.com/wiki/Category:Characters"

# Adding headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    characters = soup.find_all('a', class_='category-page__member-link')

    # Write the data to a CSV file
    with open('harry_potter_characters.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Link'])

        for character in characters:
            character_name = character.get_text()
            character_link = "https://harrypotter.fandom.com" + character.get('href')
            writer.writerow([character_name, character_link])

    print("Character names saved successfully! Data saved to harry_potter_characters.csv.")
else:
    print(f"Error: Could not retrieve the page. Status code: {response.status_code}")
