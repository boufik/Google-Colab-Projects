# 1. Auxiliary Function
from random import randrange
from math import floor

def simulate(prob, SIMS):

  wins = []
  for SIM in range(1, SIMS+1):
      # print(f"**** SIM {SIM} ****")
      counter = 0
      for sim in range(SIM):
          r = randrange(100)
          S = range(floor(100 * prob))
          if r in S:
              counter = counter + 1
      wins.append(counter)
  return wins


# 2. Display Function
import matplotlib.pyplot as plt

def display(SIMS, wins):

    x = list(range(1, SIMS+1))
    y = [prob * elem for elem in x]
    plt.plot(x, y)
    plt.plot(x, wins)
    plt.xlabel("Iterations")
    plt.ylabel("Wins")
    plt.title(f"prob = {prob}")
    plt.legend([f"y = {prob}x", "simulation"])
    plt.show()


# 3. For Loop
prob_list = [0.01, 0.05, 0.1, 0.2, 0.5]
SIMS = 200

for prob in prob_list:
    wins = simulate(prob, SIMS)
    display(SIMS, wins)
