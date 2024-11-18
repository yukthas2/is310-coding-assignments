from rich.console import Console
from rich.table import Table
import os
import json  

console = Console()

console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Example Movies")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right")

# Add some example movie data
table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

console.print(table)

def collect_movie_data():
    movies = []
    while True:
        console.print("\n[bold cyan]Enter your movie details:[/bold cyan]")
        title = console.input("Enter the title of the movie: ")
        release_date = console.input("Enter the release date of the movie: ")
        box_office = console.input("Enter the box office earnings of the movie: ")

        console.print("\n[bold yellow]You entered:[/bold yellow]")
        console.print(f"Title: {title}")
        console.print(f"Release Date: {release_date}")
        console.print(f"Box Office: {box_office}")
        confirm = console.input("Is this information correct? (yes/no): ").lower()

        if confirm == "yes":
            movies.append({"Title": title, "Release Date": release_date, "Box Office": box_office})
        else:
            console.print("[red]Let's try entering the data again...[/red]")

        add_more = console.input("Do you want to add another movie? (yes/no): ").lower()
        if add_more != "yes":
            break

    return movies

def save_data_to_file(movies):
    
    file_path = os.path.join(os.getcwd(), "movies_data.json")
    with open(file_path, "w") as file:
        json.dump(movies, file, indent=4)

    console.print(f"\n[green]Data has been saved to {file_path}[/green]")

if __name__ == "__main__":
    movie_data = collect_movie_data()
    
    
    save_data_to_file(movie_data)

