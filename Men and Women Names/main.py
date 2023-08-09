import pandas as pd
from bs4 import BeautifulSoup

# Read the HTML file
with open('./table_only.html', 'r') as file:
    html_content = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table and extract its rows
table = soup.find('table')
rows = table.find_all('tr')

# Extract data from the table and create a list of dictionaries
data = []
for row in rows:
    columns = row.find_all(['th', 'td'])
    row_data = [column.get_text(strip=True) for column in columns]
    data.append(row_data)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
print(df.head())
# Save the DataFrame to a CSV file
df.to_csv('./dataframe.csv', index=False, header=False)


andrika = ['Σ', 'Λ', 'Ν', 'Ρ']
new_df = df.loc[:, [2, 3]]
print('\n\n', new_df)

cols = list(new_df.columns)
print(cols)
new_df.to_csv('./new_dataframe.csv', index=False, header=False)

new = pd.read_csv("./new2.csv")
print(new)

LEN = new['Name'].count()
men = pd.DataFrame(columns=['Name', 'Count'])
women = pd.DataFrame(columns=['Name', 'Count'])
# print(men, '\n\n')

for index in range(len(new)):
    name = new.loc[index, 'Name']
    appearances = new.loc[index, 'Number']
    # print(name, appearances)
    if name[-1] in andrika:
        new_row = {'Name': name, 'Count' : appearances}
        men = men.append(new_row, ignore_index=True)
    else:
        new_row = {'Name': name, 'Count' : appearances}
        women = women.append(new_row, ignore_index=True)

print("There are TOTALLY {} entries".format(LEN))

print(men.head(), '\n\n')
print(women.head(), '\n\n')
MEN_COUNT = men['Count'].count()
WOMEN_COUNT = women['Count'].count()
print(MEN_COUNT, WOMEN_COUNT)
MEN_APP = men['Count'].sum()
WOMEN_APP = women['Count'].sum()
print(MEN_APP, WOMEN_APP)

dict_men = {}
for row in range(len(men)):
    name = men.loc[row, 'Name']
    count = 100 * men.loc[row, 'Count'] / MEN_APP
    dict_men[name] = count

dict_women = {}
for row in range(len(women)):
    name = women.loc[row, 'Name']
    count = 100 * women.loc[row, 'Count'] / WOMEN_APP
    dict_women[name] = count

print(dict_men, '\n\n', dict_women)

import matplotlib.pyplot as plt

keys1 = list(dict_men.keys())
values1 = list(dict_men.values())
keys2 = list(dict_women.keys())
values2 = list(dict_women.values())

plt.bar(keys1[:5], values1[:5])
plt.show()
plt.bar(keys2[:5], values2[:5])
plt.show()
