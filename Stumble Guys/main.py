# *****************************************************************************************************
# *****************************************************************************************************
# *****************************************************************************************************

from math import floor
from numpy.random import default_rng
from random import randrange
def simulate(rows, cols):

    rows = 4
    cols = 8
    array = randint(low=1, high=2, size=(rows, cols))
    rng = default_rng()
    # Half of the guys are eliminated
    ALL = rows * cols
    ELIM1 = floor(ALL / 2)
    ELIM2 = floor(ALL / 4)

    # 1a. Create a 1D list with indeces
    elim_indeces = rng.choice(ALL, size=ELIM1, replace=False)
    elim_indeces = list(sorted(elim_indeces))
    # 1b. 2D indeces
    _2D_indeces_1 = []
    for elem in elim_indeces:
        row = elem // cols
        col = elem - row * cols
        _2D_indeces_1.append([row, col])
    # 1c. I replace the 1s in array with 0s, but only for these [row, col] pairs
    for elem in _2D_indeces_1:
        array[elem[0], elem[1]] = 0
    # 1d. Find out in how many columns there are survivors
    S1 = sum(array)
    C1 = 0
    for elem in S1:
        if elem:
            C1 = C1 + 1

    # 2a. Create the 2nd list with indeces. The new ones must be different from the previous ones
    elim_indeces2 = []
    for i in range(ELIM2):
        r = randrange(ALL)
        while (r in elim_indeces) or (r in elim_indeces2):
            r = randrange(ALL)
        elim_indeces2.append(r)

    elim_indeces2 = sorted(elim_indeces2)
    # 2b. 2D indeces
    _2D_indeces_2 = []
    for elem in elim_indeces2:
        row = elem // cols
        col = elem - row * cols
        _2D_indeces_2.append([row, col])
    # 2c. I replace the 1s in array with 0s, but only for these [row, col] pairs
    for elem in _2D_indeces_2:
        array[elem[0], elem[1]] = 0
    # 2d. Find out in how many columns there are survivors
    S2 = sum(array)
    C2 = 0
    for elem in S2:
        if elem:
            C2 = C2 + 1

    return C1, C2

# *****************************************************************************************************
# *****************************************************************************************************
# *****************************************************************************************************




from numpy.random import randint
rows = 4
cols = 8
array = randint(low=1, high=2, size=(rows, cols))
print(array)


from math import floor
from numpy.random import default_rng
rng = default_rng()
# Half of the guys are eliminated
ALL = rows * cols
ELIM1 = floor(ALL / 2)
ELIM2 = floor(ALL / 4)


# Create a 1D list with indeces
elim_indeces = rng.choice(ALL, size=ELIM1, replace=False)
elim_indeces = list(sorted(elim_indeces))
print(elim_indeces)


_2D_indeces_1 = []
for elem in elim_indeces:
    row = elem // cols
    col = elem - row * cols
    _2D_indeces_1.append([row, col])
print(_2D_indeces_1)


# I replace the 1s in array with 0s, but only for these [row, col] pairs
for elem in _2D_indeces_1:
    array[elem[0], elem[1]] = 0
print(array, '\n')

# Find out in how many columns there are survivors
S1 = sum(array)
C1 = 0
for elem in S1:
    if elem:
        C1 = C1 + 1
print(S1, C1)


from random import randrange
# Create the 2nd list with indeces. The new ones must be different from the previous ones
elim_indeces2 = []
for i in range(ELIM2):
    r = randrange(ALL)
    while (r in elim_indeces) or (r in elim_indeces2):
        r = randrange(ALL)
    elim_indeces2.append(r)
elim_indeces2 = sorted(elim_indeces2)
print(elim_indeces, '\n', elim_indeces2)


_2D_indeces_2 = []
for elem in elim_indeces2:
    row = elem // cols
    col = elem - row * cols
    _2D_indeces_2.append([row, col])
print(_2D_indeces_2)


# I replace the 1s in array with 0s, but only for these [row, col] pairs
for elem in _2D_indeces_2:
    array[elem[0], elem[1]] = 0
print(array, '\n')
# Find out in how many columns there are survivors
S2 = sum(array)
C2 = 0
for elem in S2:
    if elem:
        C2 = C2 + 1
print(S2, C2)





# *****************************************************************************************************
# *****************************************************************************************************
# *****************************************************************************************************

round1 = []
round2 = []
SIMS = 10**4
rows = 4
cols = 8
for sim in range(SIMS):
    C1, C2 = simulate(rows, cols)
    round1.append(C1)
    round2.append(C2)
print(round1, '\n', round2)

dict1 = {num : round1.count(num) for num in set(round1)}
keys1 = list(dict1.keys())
keys1 = sorted(keys1)
dict1_new = {key : dict1[key] / SIMS for key in keys1}
dict2 = {num : round2.count(num) for num in set(round2)}
keys2 = list(dict2.keys())
keys2 = sorted(keys2)
dict2_new = {key : dict2[key] / SIMS for key in keys2}
dict1 = {key : f"{round(100*dict1_new[key], 2)} %" for key in list(dict1_new.keys())}
dict2 = {key : f"{round(100*dict2_new[key], 2)} %" for key in list(dict2_new.keys())}
print(f"After round 1 ({ALL-ELIM1} players proceeding):\n", dict1, '\n\n', \
      f"After round 2 ({ALL-ELIM1-ELIM2} players proceeding):\n", dict2)

import matplotlib.pyplot as plt
import seaborn as sns
plt.hist(round1)
plt.show()
sns.kdeplot(round1)
plt.show()
plt.hist(round2)
plt.show()
sns.kdeplot(round2)
plt.show()
# *****************************************************************************************************
# *****************************************************************************************************
# *****************************************************************************************************
