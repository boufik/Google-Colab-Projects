# 1. Basics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 1a. Define the traits and their types
red = ['Επιθετικός', 'Φιλόδοξος', 'Με ισχυρή θέληση', 'Προσανατολισμένος στον στόχο', 'Πιεστικός', 'Καλός στην επίλυση των προβλημάτων', 'Πρωτοπόρος', 'Αποφασιστικός', 'Καινοτόμος', 'Ανυπόμονος', 'Ελεγκτικός', 'Πειστικός', 'Προσανατολισμένος στην απόδοση', 'Δυνατός', 'Προσανατολισμένος στα αποτελέσματα', 'Πρωτεργάτης', 'Ταχύς', 'Συνεπής', 'Έντονος', 'Ισχυρογνώμων', 'Ευθύς', 'Ανεξάρτητος']
red_types = ['Α', 'Θ', 'Θ', 'Θ', 'Α', 'Θ', 'Θ', 'Θ', 'Θ', 'Α', 'Α', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Ο', 'Α', 'Θ', 'Θ']
yellow = ['Ομιλητικός', 'Ενθουσιώδης', 'Πειστικός ', 'Δημιουργικός', 'Αισιόδοξος', 'Κοινωνικός', 'Αυθόρμητος', 'Εκφραστικός', 'Γοητευτικός', 'Γεμάτος ζωτικότητα', 'Εγωκεντρικός', 'Ευαίσθητος', 'Ευπροσάρμοστος', 'Εμπνευσμένος', 'Επιζητά την προσοχή', 'Ενθαρρυντικός', 'Επικοινωνιακός', 'Ευέλικτος', 'Ανοιχτός', 'Φιλικός', 'Ευφάνταστος', 'Καλόβολος']
yellow_types = ['Ο', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Α', 'Θ', 'Θ', 'Θ', 'Α', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ']
green = ['Υπομονετικός', 'Χαλαρός', 'Με αυτοέλεγχο', 'Αξιόπιστος', 'Συγκροτημένος', 'Πιστός', 'Σεμνός', 'Με κατανόηση', 'Αργόσυρτος', 'Σταθερός', 'Εγκρατής', 'Διακριτικός', 'Υποστηρικτικός', 'Καλός ακροατής', 'Βοηθητικός', 'Παραγωγός', 'Επίμονος', 'Απρόθυμος', 'Σκεπτικός', 'Κρύβει συναισθήματα', 'Σκέφτεται τους άλλους', 'Στοργικός']
green_types = ['Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Α', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Θ', 'Α', 'Α', 'Ο', 'Α', 'Θ', 'Θ']
blue = ['Ευσυνείδητος', 'Συστηματικός', 'Απόμακρος', 'Σωστός', 'Συμβατικός', 'Μοιάζει ανασφαλής', 'Αντικειμενικός', 'Συγκροτημένος', 'Αναλυτικός', 'Τελειομανής', 'Χρειάζεται χρόνο', 'Σκεπτικός ', 'Μεθοδικός', 'Αναζητά γεγονότα', 'Προσανατολισμένος στην ποιότητα', 'Ελέγχει εξονυχιστικά', 'Ακολουθεί κανόνες', 'Λογικός', 'Αμφισβητίας', 'Ενδελεχής', 'Στοχαστικός', 'Επιφυλακτικός']
blue_types = ['Θ', 'Θ', 'Α', 'Θ', 'Ο', 'Α', 'Θ', 'Θ', 'Θ', 'Ο', 'Ο', 'Θ', 'Θ', 'Θ', 'Θ', 'Ο', 'Θ', 'Θ', 'Ο', 'Θ', 'Θ', 'Ο']


LEN1 = len(red)
LEN2 = len(yellow)
LEN3 = len(green)
LEN4 = len(blue)
LEN5 = len(red_types)
LEN6 = len(yellow_types)
LEN7 = len(green_types)
LEN8 = len(blue_types)
LEN = LEN1 + LEN2 + LEN3 + LEN4

print(80 * "-")
if LEN1 == LEN5 and LEN2 == LEN6 and LEN3 == LEN7 and LEN4 == LEN8:
    print("Personality traits:\n")
    print(f"{LEN1} red\n{LEN2} yellow\n{LEN3} green\n{LEN4} blue")
    print(f"{LEN} total")
print(80 * "-", '\n\n')

# 1b. Concatenate the lists
traits = red + yellow + green + blue
colors = ["Κόκκινο" for __ in range(LEN1)] + ["Κίτρινο" for __ in range(LEN1)] + ["Πράσινο" for __ in range(LEN1)] + ["Μπλε" for __ in range(LEN1)]
types = red_types + yellow_types + green_types + blue_types
type_dict = {'Α':'Αρνητικό', 'Θ':'Θετικό', 'Ο':'Ουδέτερο'}
types = [type_dict[type] for type in types]


# 1c. Create an initial dataframe with 'ΟΧΙ' in the 4th column
print(80 * "-")
print(f"\nInitial Dataframe")
my_dict = {'Trait': traits, 'Color': colors, 'Type': types}
df = pd.DataFrame(my_dict)
print(df)
print(80 * "-")



# 2. Random input
from random import randrange

name = "Random User"
ratings = [randrange(11) for _ in range(LEN)]
df = pd.DataFrame(my_dict)
df['Rating (?/10)'] = ratings
print(df)



# 3. Input from the user (88 ratings in personality traits)
ratings = []

name = input("Enter your name here: ")
for trait in traits:
    rating = float(input(f"{trait} (?/10) ----> "))
    while rating < 0 or rating > 10:
        print("Invalid input")
        rating = float(input(f"{trait} (?/10) ----> "))
    ratings.append(rating)

df = pd.DataFrame(my_dict)
df['Rating (?/10)'] = ratings
print(df)



# 4. Pretty Print
def pretty_print(my_dict, print_LENS=False, print_decimals=False, is_perc=False, print_rating=False):
    for key, value in my_dict.items():

        if is_perc:
            value = 100 * value

        if key == 'Μπλε':
            print(f"{key}    --->  ", end='')
            if print_decimals:
                print(f"{value:.2f}", end='')
            else:
                print(f"{value}", end='')
            if is_perc:
                print(f" %", end='')
            if print_LENS:
                print(f" / 22", end='')
            if print_rating:
                print(f" / 10.00", end='')

        else:
            print(f"{key} --->  ", end='')
            if print_decimals:
                print(f"{value:.2f}", end='')
            else:
                print(f"{value}", end='')
            if is_perc:
                print(f" %", end='')
            if print_LENS:
                print(f" / 22", end='')
            if print_rating:
                print(f" / 10.00", end='')

        print()



# 5. Create the 3 basic dictionaries
LENS = [LEN1, LEN2, LEN3, LEN4]
num_colors = df['Color'].nunique()
colors = list(df['Color'].unique())

# First dictionary:  Add +1 in each color "counter", when a trait rating is above 5
# example = {red:20, yellow:15, green:12, blue:14}
colors_dict = {color:0 for color in colors}
# Second dictionary: Find the mean rating of every trait in a color
# example = {red:9.5, yellow:7.5, green:6.2, blue:7.0}
colors_avg_dict = {color:5 for color in colors}

for color in colors:
    df2 = df[df['Color'] == color]
    for i, rating in enumerate(df2['Rating (?/10)']):
        if rating >= 5:
            colors_dict[color] = colors_dict[color] + 1
    avg = df2['Rating (?/10)'].mean()
    colors_avg_dict[color] = avg

colors_perc_dict = {color:colors_dict[color]/LENS[i] for i, color in enumerate(colors)}



# 6. Some easy statistics
import numpy as np

df_good_total = df[df['Type'] == 'Θετικό']
df_bad_total = df[df['Type'] == 'Αρνητικό']
df_neutral_total = df[df['Type'] == 'Ουδέτερο']
num_good_total = len(df_good_total)
num_bad_total = len(df_bad_total)
num_neutral_total = len(df_neutral_total)
# print(f"Number of good traits: {num_good_total}")
# print(f"Number of bad traits: {num_bad_total}")
# print(f"Number of neutral traits: {num_neutral_total}")


df_good_user = df[(df['Type'] == 'Θετικό') & (df['Rating (?/10)'] >= 5)]
df_bad_user = df[(df['Type'] == 'Αρνητικό') & (df['Rating (?/10)'] >= 5)]
df_neutral_user = df[(df['Type'] == 'Ουδέτερο') & (df['Rating (?/10)'] >= 5)]
num_good_user = len(df_good_user)
num_bad_user = len(df_bad_user)
num_neutral_user = len(df_neutral_user)
# print(f"Number of good traits (user): {num_good_user}")
# print(f"Number of bad traits (user): {num_bad_user}")
# print(f"Number of neutral traits (user): {num_neutral_user}")


print(f"For user '{name}':\n")
print(80 * "-")
print(f"Positive traits: {num_good_user:2d} / {num_good_total:2d} = {100*num_good_user/num_good_total:.2f}%")
print(f"Negative traits: {num_bad_user:2d} / {num_bad_total:2d} = {100*num_bad_user/num_bad_total:.2f}%")
print(f"Neutral traits:  {num_neutral_user:2d} / {num_neutral_total:2d} = {100*num_neutral_user/num_neutral_total:.2f}%")
print(80 * "-", '\n')

print(80 * "-")
print("Interpretation 1 - Which traits do I have?")
pretty_print(colors_dict, True, False, False, False)
print("\nInterpretation 1 - Which traits do I have (percentage)?")
pretty_print(colors_perc_dict, False, True, True, False)
print(80 * "-")
print('\n')
print(80 * "-")
print("Interpretation 2 - Mean rating of color traits")
pretty_print(colors_avg_dict, False, True, False, True)
print(80 * "-")



# 7. Normalization - Create 2 auxiliary dictionaries
# Normalization processes
SUM1 = 0
for value in colors_perc_dict.values():
    SUM1 = SUM1 + value
normalized1 = {color:value/SUM1 for color, value in colors_perc_dict.items()}


SUM2 = 0
for value in colors_avg_dict.values():
    SUM2 = SUM2 + value
normalized2 = {color:value/SUM2 for color, value in colors_avg_dict.items()}


# Displays
print(80 * "-")
print("Normalization - Interpretation 1 - Which traits do I have?")
pretty_print(normalized1, False, True, True, False)
print(80 * "-", '\n\n')
print(80 * "-")
print("Normalization - Interpretation 2 - Mean rating of color traits")
pretty_print(normalized2, False, True, True, False)
print(80 * "-", '\n\n')



# 8. Bar diagrammes and pie charts
import seaborn as sns
import matplotlib.pyplot as plt
colors_for_plot = ['#FF0000', '#FFFF00','#00FF00', '#0000FF']


# Interpretation 1
print(colors_perc_dict, '\n', normalized1, '\n')
fig, ax = plt.subplots()
mylabels1 = [f"{100*elem:.2f}%" for elem in list(colors_perc_dict.values())]
plt.bar(colors_perc_dict.keys(), colors_perc_dict.values(), color=colors_for_plot, label=mylabels1)
plt.ylabel('Ποσοστό')
plt.title(f"Interpretation 1 for {name}")
plt.legend(mylabels1)
ax.plot([-0.5, 4.5], [1, 1], "k--")
plt.show()
print('\n')

y1 = np.array(list(normalized1.values()))
mylabels1 = [f"{100*elem:.2f}%" for elem in y1]
plt.pie(y1, colors=colors_for_plot)
plt.legend(mylabels1)
plt.title(f"Interpretation 1 for {name}")
plt.show()



# Interpretation 2
print(colors_avg_dict, '\n', normalized2, '\n')
fig, ax = plt.subplots()
mylabels2 = [f"{elem:.2f}" for elem in list(colors_avg_dict.values())]
plt.bar(colors_avg_dict.keys(), colors_avg_dict.values(), color=colors_for_plot, label=mylabels2)
plt.ylabel('Ποσοστό')
plt.title(f"Interpretation 2 for {name}")
plt.legend(mylabels2)
ax.plot([-0.5, 4.5], [10, 10], "k--")
plt.show()
print('\n')

y2 = np.array(list(normalized2.values()))
mylabels2 = [f"{100*elem:.2f}%" for elem in y2]
plt.pie(y2, colors=colors_for_plot)
plt.legend(mylabels2)
plt.title(f"Interpretation 2 for {name}")
plt.show()
