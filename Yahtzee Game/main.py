# 1. Global variables
valid_combs = ["1. Ones", "2. Twos", "3. Threes", "4. Fours", "5. Fives", "6. Sixes", "7. Three of a kind", "8. Four of a kind", "9. Full House", "10.Small Straight", "11. Large Straight", "12. Yahtzee", "13. Chance"]
valid_rules = ["Sum of aces", "Sum of twos", "Sum of threes", "Sum of fours", "Sum of fives", "Sum of sixes", "Sum of all dice", "Sum of all dice", "25", "30", "40", "50", "Sum of all dice"]
LEN = len(valid_combs)


# 2. Auxiliary Functions
def count(pentada):
    # Count how many 1s, 2s, ...., 6s there are
    counters = list()
    for i in range(1, 7):
        counters.append(pentada.count(i))
    return counters

def score(pentada, rule):

    if rule in list(range(1, 7)):
        return rule * pentada.count(rule)

    elif rule == 7:
      # Three of a kind
      counters = count(pentada)
      return sum(pentada) if ((3 in counters) or (4 in counters) or (5 in counters)) else 0

    elif rule == 8:
        # Four of a kind
        counters = count(pentada)
        return sum(pentada) if ((4 in counters) or (5 in counters)) else 0

    elif rule == 9:
        # Full House
        counters = count(pentada)
        counters = sorted(counters, reverse=True)
        return 25 if counters == [3, 2, 0, 0, 0, 0] else 0

    elif rule == 10:
        # Small Straight = 1-2-3-4 or 2-3-4-5 or 3-4-5-6
        pentada = set(pentada)
        valids = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
        for valid in valids:
            if valid.issubset(pentada):
                return 30
        return 0

    elif rule == 11:
        # Large Straight = 1-2-3-4-5 or 2-3-4-5-6
        counters = count(pentada)
        counters = sorted(counters, reverse=True)
        return 40 if counters == [1, 1, 1, 1, 1, 0] else 0

    elif rule == 12:
        # Yahtzee
        counters = count(pentada)
        counters = sorted(counters, reverse=True)
        return 50 if counters == [5, 0, 0, 0, 0, 0] else 0

    elif rule == 13:
        # Chance
        return sum(pentada)

num_combs = list(range(1, LEN + 1))
def decide(num_combs_used, dices, player, points):
    declaration = ""
    for num_comb in num_combs:
        if num_comb not in num_combs_used:
            declaration = declaration + valid_combs[num_comb - 1] + ", "
    if declaration:
        declaration = declaration[:-2]
    print("!!!! Available combinations !!!!\n", declaration)

    rule = int(input("Select combination: "))
    while rule in num_combs_used:
        rule = int(input("Select combination: "))

    num_combs_used.append(rule)
    new_points = score(dices, rule)
    COMB = valid_combs[rule - 1]
    STR = COMB[3:]
    points = points + new_points
    print(f"{player} scored {new_points} points with {STR} ----> Total points = {points}")
    return points, num_combs_used


# 3. Playing Functions
from random import randrange
import copy
def roll(N):
    return [randrange(1, 7) for i in range(N)]

rerolls_permitted = 2

def show(dices, round, rerolls_used, player):
    # print(40 * "*")
    print(f"{rerolls_permitted - rerolls_used} rerolls left for {player} in round {round}:")
    dices_str = [str(elem) for elem in dices]
    dice_show = " - ".join(dices_str)
    print(f"{player} threw:\t {dice_show}\n")

def rerolls0(player, rerolls_used, N, round, points, num_combs_used):
    print(f"\n\n----> {player}'s turn ({points} points)    -    Combinations used = {num_combs_used}")
    dices = roll(N)
    show(dices, round, rerolls_used, player)
    return dices

def rerolls1(player, rerolls_used, N, round, dices, positions):
    positions = positions.split(", ")
    positions = [int(position) for position in positions]
    new_rolls = roll(len(positions))
    # Checking if positions are between 1 and N - Invalid input, then dices are not changed
    for position in positions:
        if position not in list(range(1, N+1)):
            return dices
    # Changing the dices
    for i in range(len(positions)):
        index = positions[i] - 1
        value = new_rolls[i]
        dices[index] = value
    show(dices, round, rerolls_used, player)
    return dices


# MAIN FUNCTION
players = ["Thomas", "PC"]
num_combs_used_list = [[], []]
points_list = [0, 0]
N = 5
bold_start = "\033[1m"
bold_end = "\033[0;0m"

for round in list(range(1, LEN + 1)):
    print(20 * "*", 20 * "*", sep=f" Round {round} ", end="\n")
    for i, player in enumerate(players):

          num_combs_used = num_combs_used_list[i]
          points = points_list[i]

          rerolls_used = 0
          dices = rerolls0(player, rerolls_used, N, round, points, num_combs_used)
          positions = input("Positions to reroll: ")
          if positions == "":
              # print("Time to decide (0 rerolls used)\n")
              points, num_combs_used = decide(num_combs_used, dices, player, points)
              continue
          else:
              rerolls_used = 1

          dices = rerolls1(player, rerolls_used, N, round, dices, positions)
          positions = input("Positions to reroll:\n")
          if positions == "":
              # print("Time to decide (1 reroll used)\n")
              points, num_combs_used = decide(num_combs_used, dices, player, points)
              continue
          else:
              rerolls_used = 2

          dices = rerolls1(player, rerolls_used, N, round, dices, positions)
          points, num_combs_used = decide(num_combs_used, dices, player, points)

          # UPDATE THE VALUES OF LISTS
          num_combs_used_list[i] = num_combs_used
          points_list[i] = points
    print("\n\n\n\n")
