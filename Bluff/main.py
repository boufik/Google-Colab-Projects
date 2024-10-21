# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)



# AUXILIARY FUNCTIONS
def roll(no_dices):
    return np.random.randint(1, 7, size=no_dices)


def how_many(num_list, no_dices):
    # Random dices throw
    dices = roll(no_dices)
    SUM = 0
    for dice in dices:
        if dice in num_list:
            SUM = SUM + 1
    return SUM




def probability_to_win(values, threshold):
    LEN = len(values)
    SUM = 0
    for value in values:
        # value represents a random round throw - 1 round from the many SIMS we ran
        if value >= threshold:
            SUM = SUM + 1
    return 100 * SUM / LEN


def analyze_probabilities(avg_rounded, no_dices, num_list, values):
    # If there are more than 30 dices, I do not print anything
    if no_dices <= 30:

        # 1. Determine the range of the investigation for probabilities
        low = -1000
        high = -1000
        if no_dices in list(range(1, 11)):
            low = 0
            high = no_dices
        elif no_dices in list(range(11, 21)):
            low = max(avg_rounded - 4, 0)
            high = min(avg_rounded + 4, no_dices)
        else:
            low = max(avg_rounded - 5, 0)
            high = min(avg_rounded + 5, no_dices)

        # 2. Call the function above
        prob_list = []
        for threshold in list(range(low, high+1)):
            prob = probability_to_win(values, threshold)
            prob_list.append(prob)
            print(f"Probability to win if I say that there are AT LEAST {threshold}/{no_dices} dices with {num_list}: {prob}%", end=4*' ')
            if threshold == avg_rounded:
                print(f"----> avg_rounded = {avg_rounded} <----")
            else:
                print()
        print('\n')

        # 3. Create a dictionary and then return it
        keys = list(range(low, high+1))
        values = prob_list
        dictionary = dict(zip(keys, values))
        return dictionary


def plot_prob_list(dictionary, avg_rounded, num_list, no_dices):
    prob_in_avg_rounded = dictionary[avg_rounded]
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    # 1st plot
    plt.plot(keys, values, 'blue')
    # 2nd plot
    plt.plot(avg_rounded, prob_in_avg_rounded, 'o', color='red', markersize=12)
    # 3rd plot
    plt.plot(keys, len(keys) * [prob_in_avg_rounded], 'r--')
    # 4th plot
    plt.plot(keys, values, 'bo')
    plt.title(f"Searching how many {num_list} there are in {no_dices} dices (AT LEAST)")
    plt.xlabel(f"Dices showing {num_list} (AT LEAST)")
    plt.ylabel("Probability [%]")
    plt.legend(["Dices", "Average Value calculated"])
    plt.show()



def simulate(SIMS, num_list, no_dices):
    values =[]
    for SIM in range(SIMS):
        values.append(how_many(num_list, no_dices))
    avg = sum(values) / SIMS
    avg_rounded = round(avg)
    st = f"How many {num_list} in {no_dices} dices ----> avg_rounded = {avg_rounded} (rounded from {round(avg, 3)})"
    print(len(st) * "~", '\n', st, '\n', len(st) * "~", '\n')
    dictionary = analyze_probabilities(avg_rounded, no_dices, num_list, values)
    st2 = str(dictionary)
    print(len(st2) * "~", '\n', st2, '\n', len(st2) * "~", '\n')
    plot_prob_list(dictionary, avg_rounded, num_list, no_dices)


# MAIN FUNCTION
num_list = [5, 6]
no_dices = 15
SIMS = 10**4
simulate(SIMS, num_list, no_dices)
