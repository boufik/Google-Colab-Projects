import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Check if the request was successful
if response.status_code == 200:
    # Content of the HTML page
    html_content = response.text

    # Save the HTML content to a file
    with open("website.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    print("HTML content downloaded and saved as 'website.html'")
else:
     print(f"Failed to download HTML content. Status code: {response.status_code}")

# Find the HTML elements containing the headlines
headline_elements = soup.find_all("h3", class_="gs-c-promo-heading__title")

# Extract and print the headlines
print("Top headlines from BBC News:")
for index, headline_element in enumerate(headline_elements, start=1):
    headline_text = headline_element.get_text()
    print(f"{index}. {headline_text}")
