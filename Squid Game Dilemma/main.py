# 1. Rules

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")
from matplotlib.colors import LinearSegmentedColormap

def pick_shape():
    return random.choice(["C", "T", "R"])

def pick_remaining_shapes():
    return random.choice(["C", "T"])

def select_random_finalist():
    return random.choice(["A", "B"])



# 2. Special Condition

# !!!! The function returns the percentages in M-A-B order for EVERY scenario

def run(SIMS, scenario):
    winsA = 0
    winsB = 0
    winsM = 0
    for SIM in range(SIMS):
        winners = scenario()
        if "A" in winners:
            winsA += 1
        if "B" in winners:
            winsB += 1
        if "M" in winners:
            winsM += 1
    percM = 100 * winsM / SIMS
    percA = 100 * winsA / SIMS
    percB = 100 * winsB / SIMS
    return percM, percA, percB

# !!!! The function returns the percentages in M-A-B order for EVERY scenario



# 3. Auxiliary Functions

def plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb):

    # Create two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    # First subplot
    bars1 = ax1.bar(x, y1, color='skyblue')
    ax1.set_title(f"Scenario {scenario_id} - {scenario_abb} - Simulations")
    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{height:.2f}%',
                ha='center', va='center', color='black', fontsize=10)

    # Second subplot
    bars2 = ax2.bar(x, y2, color='lightgreen')
    ax2.set_title(f"Scenario {scenario_id} - {scenario_abb} - Theoretical")
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{height:.2f}%',
                ha='center', va='center', color='black', fontsize=10)
    plt.show()



# 4. The six identified scenarios

# Scenario 1
# S1 = MAB

def scenario1(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "M" qualifies and determines randomly the next finalist
        winners.append("M")
        winner2 = select_random_finalist()
        winners.append(winner2)
        if verbose:
            print(f"Player 1: M = C ---> Qualified!!!\nPlayer 2: A = ?\nPlayer 3: B = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "M" is eliminated
        winners.append("A")
        winners.append("B")
        if verbose:
            print(f"Player 1: M = T ---> Eliminated...\nPlayer 2: A = ?\nPlayer 3: B = ?\n\nWinners = {winners}")
    else:
        # Player "M" has picked the rectange, so he is waiting for the pick of player "A"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "A" qualifies and selects "B" as the next finalist
            winners.append("A")
            winners.append("B")
            if verbose:
                print(f"Player 1: M = R ---> Waiting...\nPlayer 2: A = C ---> Qualified!!!\nPlayer 3: B = ?\n\nWinners = {winners}")
        else:
            # Player "A" is eliminated, because he picked "T", so players "M" and "b" qualify
            winners.append("M")
            winners.append("B")
            if verbose:
                print(f"Player 1: M = R ---> Waiting...\nPlayer 2: A = T ---> Eliminated...\nPlayer 3: B = ?\n\nWinners = {winners}")
    return winners

scenario1(verbose=True)

SIMS = 10**4
sc1_sim_percM, sc1_sim_percA, sc1_sim_percB = run(SIMS, scenario1)
prob1 = np.array([1/2, 2/3, 5/6])
sc1_thr_percM, sc1_thr_percA, sc1_thr_percB = list(100 * prob1)
print(f"Scenario 1 - MAB - Simulations\nM : {sc1_sim_percM:.2f}%\nA : {sc1_sim_percA:.2f}%\nB : {sc1_sim_percB:.2f}%\n")
print(f"Scenario 1 - MAB - Thoeretical\nM : {sc1_thr_percM:.2f}%\nA : {sc1_thr_percA:.2f}%\nB : {sc1_thr_percB:.2f}%")

y1 = [sc1_sim_percM, sc1_sim_percA, sc1_sim_percB]
y2 = [sc1_thr_percM, sc1_thr_percA, sc1_thr_percB]
x = list(range(len(y1)))
labels = ["M", "A", "B"]
scenario_id = 1
scenario_abb = "MAB"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# Scenario 2
# S2 = MBA

def scenario2(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "M" qualifies and determines randomly the next finalist
        winners.append("M")
        winner2 = select_random_finalist()
        winners.append(winner2)
        if verbose:
            print(f"Player 1: M = C ---> Qualified!!!\nPlayer 2: B = ?\nPlayer 3: A = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "M" is eliminated
        winners.append("B")
        winners.append("A")
        if verbose:
            print(f"Player 1: M = T ---> Eliminated...\nPlayer 2: B = ?\nPlayer 3: A = ?\n\nWinners = {winners}")
    else:
        # Player "M" has picked the rectange, so he is waiting for the pick of player "B"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "B" qualifies and selects "A" as the next finalist
            winners.append("B")
            winners.append("A")
            if verbose:
                print(f"Player 1: M = R ---> Waiting...\nPlayer 2: B = C ---> Qualified!!!\nPlayer 3: A = ?\n\nWinners = {winners}")
        else:
            # Player "B" is eliminated, because he picked "T", so players "M" and "A" qualify
            winners.append("M")
            winners.append("A")
            if verbose:
                print(f"Player 1: M = R ---> Waiting...\nPlayer 2: B = T ---> Eliminated...\nPlayer 3: A = ?\n\nWinners = {winners}")
    return winners

scenario2(verbose=True)

SIMS = 10**4
sc2_sim_percM, sc2_sim_percA, sc2_sim_percB = run(SIMS, scenario2)
prob2 = np.array([1/2, 2/3, 5/6])
sc2_thr_percM, sc2_thr_percB, sc2_thr_percA = list(100 * prob2)
print(f"Scenario 2 - MBA - Simulations\nM : {sc2_sim_percM:.2f}%\nB : {sc2_sim_percB:.2f}%\nA : {sc2_sim_percA:.2f}%\n")
print(f"Scenario 2 - MBA - Theoretical\nM : {sc2_thr_percM:.2f}%\nB : {sc2_thr_percB:.2f}%\nA : {sc2_thr_percA:.2f}%")

y1 = [sc2_sim_percM, sc2_sim_percB, sc2_sim_percA]
y2 = [sc2_thr_percM, sc2_thr_percB, sc2_thr_percA]
x = list(range(len(y1)))
labels = ["M", "B", "A"]
scenario_id = 2
scenario_abb = "MBA"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# Scenario 3
# S3 = AMB

def scenario3(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "A" qualifies and selects "B" as the second finalist
        winners.append("A")
        winners.append("B")
        if verbose:
            print(f"Player 1: A = C ---> Qualified!!!\nPlayer 2: M = ?\nPlayer 3: B = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "A" is eliminated
        winners.append("M")
        winners.append("B")
        if verbose:
            print(f"Player 1: A = T ---> Eliminated...\nPlayer 2: M = ?\nPlayer 3: B = ?\n\nWinners = {winners}")
    else:
        # Player "A" has picked the rectange, so he is waiting for the pick of player "M"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "M" qualifies and selects randomly the next finalist
            winners.append("M")
            winner2 = select_random_finalist()
            winners.append(winner2)
            if verbose:
                print(f"Player 1: A = R ---> Waiting...\nPlayer 2: M = C ---> Qualified!!!\nPlayer 3: B = ?\n\nWinners = {winners}")
        else:
            # Player "M" is eliminated, because he picked "T", so players "A" and "B" qualify
            winners.append("A")
            winners.append("B")
            if verbose:
                print(f"Player 1: A = R ---> Waiting...\nPlayer 2: M = T ---> Eliminated...\nPlayer 3: B = ?\n\nWinners = {winners}")
    return winners

scenario3(verbose=True)

SIMS = 10**4
sc3_sim_percM, sc3_sim_percA, sc3_sim_percB = run(SIMS, scenario3)
prob3 = np.array([7/12, 1/2, 11/12])
sc3_thr_percA, sc3_thr_percM, sc3_thr_percB = list(100 * prob3)
print(f"Scenario 3 - AMB - Simulations\nA : {sc3_sim_percA:.2f}%\nM : {sc3_sim_percM:.2f}%\nB : {sc3_sim_percB:.2f}%\n")
print(f"Scenario 3 - AMB - Theoretical\nA : {sc3_thr_percA:.2f}%\nM : {sc3_thr_percM:.2f}%\nB : {sc3_thr_percB:.2f}%")

y1 = [sc3_sim_percA, sc3_sim_percM, sc3_sim_percB]
y2 = [sc3_thr_percA, sc3_thr_percM, sc3_thr_percB]
x = list(range(len(y1)))
labels = ["A", "M", "B"]
scenario_id = 3
scenario_abb = "AMB"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# Scenario 4
# S4 = ABM

def scenario4(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "A" qualifies and selects "B" as the second finalist
        winners.append("A")
        winners.append("B")
        if verbose:
            print(f"Player 1: A = C ---> Qualified!!!\nPlayer 2: B = ?\nPlayer 3: M = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "A" is eliminated
        winners.append("B")
        winners.append("M")
        if verbose:
            print(f"Player 1: A = T ---> Eliminated...\nPlayer 2: B = ?\nPlayer 3: M = ?\n\nWinners = {winners}")
    else:
        # Player "A" has picked the rectange, so he is waiting for the pick of player "B"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "B" qualifies and selects "A" as the next finalist
            winners.append("A")
            winners.append("B")
            if verbose:
                print(f"Player 1: A = R ---> Waiting...\nPlayer 2: B = C ---> Qualified!!!\nPlayer 3: M = ?\n\nWinners = {winners}")
        else:
            # Player "B" is eliminated, because he picked "T", so players "A" and "M" qualify
            winners.append("A")
            winners.append("M")
            if verbose:
                print(f"Player 1: A = R ---> Waiting...\nPlayer 2: B = T ---> Eliminated...\nPlayer 3: M = ?\n\nWinners = {winners}")
    return winners

scenario4(verbose=True)

SIMS = 10**4
sc4_sim_percM, sc4_sim_percA, sc4_sim_percB = run(SIMS, scenario4)
prob4 = np.array([2/3, 5/6, 1/2])
sc4_thr_percA, sc4_thr_percB, sc4_thr_percM = list(100 * prob4)
print(f"Scenario 4 - ABM - Simulations\nA : {sc4_sim_percA:.2f}%\nB : {sc4_sim_percB:.2f}%\nM : {sc4_sim_percM:.2f}%\n")
print(f"Scenario 4 - ABM - Theoretical\nA : {sc4_thr_percA:.2f}%\nB : {sc4_thr_percB:.2f}%\nM : {sc4_thr_percM:.2f}%")

y1 = [sc4_sim_percA, sc4_sim_percB, sc4_sim_percM]
y2 = [sc4_thr_percA, sc4_thr_percB, sc4_thr_percM]
x = list(range(len(y1)))
labels = ["A", "B", "M"]
scenario_id = 4
scenario_abb = "ABM"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# Scenario 5
# S5 = BMA

def scenario5(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "B" qualifies and selects "A" as the second finalist
        winners.append("B")
        winners.append("A")
        if verbose:
            print(f"Player 1: B = C ---> Qualified!!!\nPlayer 2: M = ?\nPlayer 3: A = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "B" is eliminated
        winners.append("M")
        winners.append("A")
        if verbose:
            print(f"Player 1: B = T ---> Eliminated...\nPlayer 2: M = ?\nPlayer 3: A = ?\n\nWinners = {winners}")
    else:
        # Player "B" has picked the rectange, so he is waiting for the pick of player "A"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "M" qualifies and selects randomly the next finalist
            winners.append("M")
            winner2 = select_random_finalist()
            winners.append(winner2)
            if verbose:
                print(f"Player 1: B = R ---> Waiting...\nPlayer 2: M = C ---> Qualified!!!\nPlayer 3: A = ?\n\nWinners = {winners}")
        else:
            # Player "M" is eliminated, because he picked "T", so players "B" and "A" qualify
            winners.append("B")
            winners.append("A")
            if verbose:
                print(f"Player 1: B = R ---> Waiting...\nPlayer 2: M = T ---> Eliminated...\nPlayer 3: A = ?\n\nWinners = {winners}")
    return winners

scenario5(verbose=True)

SIMS = 10**4
sc5_sim_percM, sc5_sim_percA, sc5_sim_percB = run(SIMS, scenario5)
prob5 = np.array([7/12, 1/2, 11/12])
sc5_thr_percB, sc5_thr_percM, sc5_thr_percA = list(100 * prob5)
print(f"Scenario 5 - BMA - Simulations\nB : {sc5_sim_percB:.2f}%\nM : {sc5_sim_percM:.2f}%\nA : {sc5_sim_percA:.2f}%\n")
print(f"Scenario 5 - BMA - Theoretical\nB : {sc5_thr_percB:.2f}%\nM : {sc5_thr_percM:.2f}%\nA : {sc5_thr_percA:.2f}%")

y1 = [sc5_sim_percB, sc5_sim_percM, sc5_sim_percA]
y2 = [sc5_thr_percB, sc5_thr_percM, sc5_thr_percA]
x = list(range(len(y1)))
labels = ["B", "M", "A"]
scenario_id = 5
scenario_abb = "BMA"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# Scenario 6
# S6 = BAM

def scenario6(verbose=False):
    winners = list()
    pick1 = pick_shape()
    if pick1 == "C":
        # Player "B" qualifies and selects "A" as the second finalist
        winners.append("B")
        winners.append("A")
        if verbose:
            print(f"Player 1: B = C ---> Qualified!!!\nPlayer 2: A = ?\nPlayer 3: M = ?\n\nWinners = {winners}")
    elif pick1 == "T":
        # Player "B" is eliminated
        winners.append("A")
        winners.append("M")
        if verbose:
            print(f"Player 1: B = T ---> Eliminated...\nPlayer 2: A = ?\nPlayer 3: M = ?\n\nWinners = {winners}")
    else:
        # Player "B" has picked the rectange, so he is waiting for the pick of player "A"
        pick2 = pick_remaining_shapes()
        if pick2 == "C":
            # Player "A" qualifies and selects "B" as the next finalist
            winners.append("B")
            winners.append("A")
            if verbose:
                print(f"Player 1: B = R ---> Waiting...\nPlayer 2: A = C ---> Qualified!!!\nPlayer 3: M = ?\n\nWinners = {winners}")
        else:
            # Player "A" is eliminated, because he picked "T", so players "B" and "M" qualify
            winners.append("B")
            winners.append("M")
            if verbose:
                print(f"Player 1: B = R ---> Waiting...\nPlayer 2: A = T ---> Eliminated...\nPlayer 3: M = ?\n\nWinners = {winners}")
    return winners

scenario6(verbose=True)

SIMS = 10**4
sc6_sim_percM, sc6_sim_percA, sc6_sim_percB = run(SIMS, scenario6)
prob6 = np.array([2/3, 5/6, 1/2])
sc6_thr_percB, sc6_thr_percA, sc6_thr_percM = list(100 * prob6)
print(f"Scenario 6 - BAM - Simulations\nB : {sc6_sim_percB:.2f}%\nA : {sc6_sim_percA:.2f}%\nM : {sc6_sim_percM:.2f}%\n")
print(f"Scenario 6 - BAM - Theoretical\nB : {sc6_thr_percB:.2f}%\nA : {sc6_thr_percA:.2f}%\nM : {sc6_thr_percM:.2f}%")

y1 = [sc6_sim_percB, sc6_sim_percA, sc6_sim_percM]
y2 = [sc6_thr_percB, sc6_thr_percA, sc6_thr_percM]
x = list(range(len(y1)))
labels = ["B", "A", "M"]
scenario_id = 6
scenario_abb = "BAM"
print("\n")
plot_scenario(x, y1, y2, labels, scenario_id, scenario_abb)



# 5. Summary

# matrix = np.random.rand(6, 4)
index = ["S1 - MAB", "S2 - MBA", "S3 - AMB", "S4 - ABM", "S5 - BMA", "S6 - BAM"]
sc1 = [sc1_thr_percM, sc1_thr_percA, sc1_thr_percB]
sc2 = [sc2_thr_percM, sc2_thr_percA, sc2_thr_percB]
sc3 = [sc3_thr_percM, sc3_thr_percA, sc3_thr_percB]
sc4 = [sc4_thr_percM, sc4_thr_percA, sc4_thr_percB]
sc5 = [sc5_thr_percM, sc5_thr_percA, sc5_thr_percB]
sc6 = [sc6_thr_percM, sc6_thr_percA, sc6_thr_percB]
matrix = [sc1, sc2, sc3, sc4, sc5, sc6]
# Round the matrix float values with inline list manipulation
matrix = [[round(elem, 2) for elem in row] for row in matrix]

df = pd.DataFrame(data=matrix, columns=["M", "A", "B"], index=index)
print(df)


my_cmap = LinearSegmentedColormap.from_list("my_cmap", ["yellow", "green"])
sns.heatmap(df, cmap=my_cmap, annot=True, cbar=True, fmt=".2f")
plt.title("Scenarios vs Finalists probability")
plt.xlabel("Finalists probability (%)")
plt.ylabel("Scenarios")
plt.show()
