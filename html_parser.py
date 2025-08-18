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
    print("Failed to download HTML content - Status code = " + str(response.status_code))
