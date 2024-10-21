# Imports
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)



# AUXILIARY FUNCTIONS
def population(r, x0, LEN):
    x = list()
    x.append(x0)
    for i in range(1, LEN):
        x.append(r * x[i-1] * (1 - x[i-1]))
    return x
  
def simulate(r_list, x0, LEN, colors):
    mean_list = list()
    for i in range(len(r_list)):
        r = r_list[i]
        x = population(r, x0, LEN)
        local_maxes, local_mins = find_local_min_max(x)
        MEAN = np.mean(x)
        mean_list.append(MEAN)
        plt.plot(x, label=f"r = {r}", color=colors[i])

    for i in range(len(r_list)):
        print(f"r = {r_list[i]:.4f}: mean = {mean_list[i]:.4f}")
    plt.legend()
    plt.show()

# CHECK IF "">="" are needed instead of ">"
# Local maxes will be 2 lists in a list: 1st list will be the indeces and the 2nd one the values
def find_local_min_max(numbers):
    local_mins = [[], []]
    local_maxes = [[], []]
    if numbers[0] > numbers[1]:
        local_maxes[0].append(0)
        local_maxes[1].append(numbers[0])
    else:
        local_mins[0].append(0)
        local_mins[1].append(numbers[0])

    for i in range(1, len(numbers)-1):
        current = numbers[i]
        prev = numbers[i-1]
        next = numbers[i+1]
        if current > prev and current > next:
            local_maxes[0].append(i)
            local_maxes[1].append(current)
        if current < prev and current < next:
            local_mins[0].append(i)
            local_mins[1].append(current)
    return local_maxes, local_mins




# MAIN FUNCTION
r_list = [3.5, 3.55]
x0 = 0.2
LEN = 100
colors = ["red", "blue"]
simulate(r_list, x0, LEN, colors)

r_list = [3.5, 3.55]
x0 = 0.2
LEN = 100
colors = ["red", "blue"]


for i in range(len(r_list)):
    r = r_list[i]
    x = population(r, x0, LEN)
    local_maxes, local_mins = find_local_min_max(x)
    plt.plot(x, colors[i])
    plt.plot(local_maxes[0], local_maxes[1], color='black', linestyle='dashed')
    plt.plot(local_mins[0], local_mins[1], color='black', linestyle='dashed')
    plt.title(f"r = {r_list[i]}")
    plt.show()
    print("\n")
