from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests

# URL of the page to be loaded
#url = "https://www.uni-regensburg.de/biologie-vorklinische-medizin/molekulare-zellulaere-anatomie/mitarbeiter/index.html"
url = "https://www.uni-regensburg.de/biologie-vorklinische-medizin/neurobiologie-tierphysiologie/team-mitarbeiter/index.html"

# Fetch the content from the URL
response = requests.get(url)
webpage_content = response.content

# Parse the HTML
soup = BeautifulSoup(webpage_content, 'html.parser')

# Extracting image links and corresponding text
data = []
for row in soup.find_all('tr'):
    image_tag = row.find('img')
    if image_tag:
        image_src = image_tag.get('src')
        text_data = ' '.join(p.get_text(strip=True) for td in row.find_all('td')[1:] for p in td.find_all('p'))
        data.append((image_src, text_data))

# Displaying the extracted data
for item in data:
    print(f"Image Link: {item[0]}")
    print(f"Corresponding Information: {item[1]}\n")

