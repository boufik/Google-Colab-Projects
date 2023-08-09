from random import randrange
import matplotlib.pyplot as plt


def count_digits(DIGITS, MONTE_CARLO):

    dict = {}
    for sim in range(MONTE_CARLO):
        r = randrange(10**(DIGITS-1), 10**DIGITS)
        digits = len(set(str(r)))
        if digits not in list(dict.keys()):
            dict[digits] = 1
        else:
            dict[digits] = dict[digits] + 1

    # Sort dictionary by keys
    keys = list(dict.keys())
    keys.sort()
    sorted_dict = {key : dict[key] for key in keys}
    dict = sorted_dict
    print("{}-digit numbers: ---> {}".format(DIGITS, dict))

    # Plot
    keys = list(dict.keys())
    values = list(dict.values())
    plt.plot(keys, values)
    plt.plot()

    return dict


MONTE_CARLO = 10**5
DIGITS_LIST = list(range(3, 16))

LEGEND = ["{}-digit numbers".format(DIGITS) for DIGITS in DIGITS_LIST]
for DIGITS in DIGITS_LIST:
    dict = count_digits(DIGITS, MONTE_CARLO)
    plt.legend(LEGEND)
plt.show()
