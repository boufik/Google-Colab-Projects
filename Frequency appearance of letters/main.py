# 1. Execute a simple GET HTTP request using 'requests' library
import requests
from bs4 import BeautifulSoup
url = 'https://www.bbc.com/news/business-66217641'
# Send a GET request to the website
response = requests.get(url)


# 2. Create a .txt file that contains all the words
# Check if the request was successful
if response.status_code == 200:

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the text elements on the website (e.g., paragraphs, headers, etc.)
    text_elements = soup.find_all(text=True)
    # Filter out empty and whitespace-only elements, and exclude script tags
    sentences = [text.strip() for text in text_elements if text.strip() and text.parent.name != 'script']
    # Join the sentences with newline characters
    text_content = '\n'.join(sentences)
    # Save the text content to a .txt file
    with open('info.txt', 'w', encoding='utf-8') as file:
        file.write(text_content)
    print("Text copied from the website and saved as 'info.txt' successfully.")

else:

    print("Failed to retrieve content from the website.")


# 3. Open the recently-created file named 'info.txt'
file_path = './info.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()

# 4.Split into lines - Delete the first 6 lines
lines = file_contents.splitlines()
DELETED = 6
for _ in range(DELETED):
    lines.pop(0)
print("First 15 rows now:", lines[0:15], sep='\n')

# 5. Delete the word 'BBC' from every line
bad = 'BBC'
for index, line in enumerate(lines):
    modified = line.replace(bad, "")
    lines[index] = modified
print("First 15 rows now:", lines[0:15], sep='\n', end='\n\n')
print("Until now, we have a list with all the text lines in the website. We are only interested in the letters,")
print("so we can join all the lines together into a single one!")

# 6. Join all the lines (strings) into a new string
sep = ''
sentences = sep.join(lines)
print("Last 100 characters --->", sentences[-100:])

# 7. Keep only the letters and lowercase them
alphabet = "abcdefghijklmnopqrstuvwxyz"
sentences = sentences.lower()
sentences = [char for char in sentences if char in alphabet]
print("Last 100 characters --->", sentences[-100:])

# 8. Create a dictionary with all the unique letters and their frequency appearance
unique = {char : sentences.count(char) for char in set(sentences)}
values = list(unique.values())
SUM = sum(values)
print("Scanned a text with {} letters:".format(SUM), end='\n\n')
print(unique)
sorted_unique = sorted(unique.items())
print(sorted_unique)

# 9. Plot the frequency appearance
import numpy as np
import matplotlib.pyplot as plt

freq_app = {}
for tup in sorted_unique:
    letter = tup[0]
    app = tup[1]
    freq_app[letter] = round(100 * app / SUM, 2)
print(freq_app, end='\n\n')

keys = list(freq_app.keys())
values = list(freq_app.values())
LEN = len(freq_app)

plt.bar(keys, values)
plt.title("Frequency appearance of letters")
plt.ylabel("Frequency appearance (%)")
plt.show()

# 10. Sort by values (descending order)
app_desc = sorted(freq_app.items(), key=lambda item : item[1], reverse=True)
print(app_desc, end='\n\n')
app_desc = dict(app_desc)
new_keys = list(app_desc.keys())
new_values = list(app_desc.values())

xvalues = np.arange(0, LEN, 1)
plt.bar(xvalues, new_values)
plt.xticks(xvalues, new_keys)
plt.title("Frequency appearance of letters")
plt.ylabel("Frequency appearance (%)")
plt.show()
