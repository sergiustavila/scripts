import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise exception if the request failed
    return response.content

def extract_species_names(soup):
    # Find the table containing species. The assumption here is that species are stored in a table.
    species_table = soup.find('table', {'class': 'wikitable'})
    if not species_table:
        return []

    species_names = []

    # Loop through each row in the table, skip the header
    for row in species_table.findAll('tr')[1:]:
        species_cell = row.findAll('td')[0]
        species_name = species_cell.get_text(strip=True)
        species_names.append(species_name)

    return species_names

def save_to_file(filename, species):
    with open(filename, 'w') as f:
        for s in species:
            f.write(s + '\n')
        f.write(f'Total species count: {len(species)}\n')

def main():
    URL = 'https://en.wikipedia.org/wiki/Python_(genus)'
    html_content = fetch_wikipedia_page(URL)
    soup = BeautifulSoup(html_content, 'html.parser')

    species_names = extract_species_names(soup)
    save_to_file('python_species.txt', species_names)

if __name__ == "__main__":
    main()