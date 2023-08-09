# 1. Type of variables
a = '1234'
b = int(a)
print(type(a), type(b))

# 2. Help Built-in Function
help(round)
a = 2853.567
ndigits_list = list(range(-2, 3))
print("Rounding:", [round(a, ndigits) for ndigits in ndigits_list])

# 3. Docstrings
def least_difference(a, b, c):
    """
    Returns the smallest difference between two numbers given a, b and c. For example:

    >>> print(least_difference(5, 80, 7))
    2
    """
    return min(abs(a-b), abs(a-c), abs(b-c))

help(least_difference)
print(least_difference(10, 100, 1))


def most_difference(a, b, c):
    """
    Returns the highest difference between two numbers given a, b and c. For example:

    >>> print(most_difference(5, 80, 7))
    75
    """
    return max(abs(a-b), abs(a-c), abs(b-c))

help(most_difference)
print(most_difference(10, 100, 1))


# 4. Print Default Arguments
a = 20
b = 'Hello Friends'
c = 100
greet = "Today I'm turning"
print(a, b, c, greet)
print(a, b, c, greet, sep=" ----> ")
print()
print(b, greet, sep="... ", end = " ")
print(a, "years old")

# 5. Functions applied to functions
def add50(n):
    return n + 50
def mult50(n):
    return 50 * n

def call(func, my_list):
    return func(my_list)

print(call(add50, 2))
print(call(mult50, 2))

# 6. Argmax
def mod_5(x):
    return x % 5

my_list = [100, 51, 14]
print(my_list)
print("Which number is the biggest?", max(my_list), "Which number is the biggest modulo 5?", max(my_list, key=mod_5), sep="\n")

# 7. Lists: Access Elements
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print("First 3 planets:", planets[:3], "Last 3 planets:", planets[-3:], sep="\n")
print("All the planets except the first and the last one:", planets[1:-1])

# 8. Numbers: Attributes and Methods
x = 16
c = 15 + 3j
print(x.imag, c.imag)
z = 32
y = 0.125
print(x.bit_length(), z.bit_length())
print(z.as_integer_ratio(), y.as_integer_ratio())

# 9. Lists: Methods
print(planets, planets.index('Earth'), sep=" ---> ")
print(planets, planets.index('Pluto'), sep=" ---> ")

# 10. Upper and Lower
c1 = 'H'
c2 = 'h'
print(c1, c1.isupper(), sep=" ----> ")
print(c2, c2.isupper(), sep=" ----> ")
s1 = 'Hello in all thE coLLeagues and yOung friends!'
for char in s1:
  if char.isupper():
    print(char, end='')
print()
print(s1.upper(), s1.lower(), sep='\n')

# 11. List Comprehensions
L = [i**2 for i in range(1, 11)]
lower_than_40 = len([elem for elem in L if elem < 40])
print(L, lower_than_40)

# 12. Strings: Methods
s1 = 'Hello'
s2 = "Hello"
s3 = """Hello"""
print(s1==s2, s1==s3, s2==s3, len("\n"))
# Split
date = '30-06-2023'
print(date)
separator1 = '-'
date_split = date.split(separator1)
num, month, year = date_split
print(num, month, year)
# Join
separator2 = '/'
date2 = separator2.join(date_split)
print(date2)

# 13. Format
planet = 'Mars'
position = planets.index(planet) + 1
# 13.1. Easy Example
print(planet + " is the " + str(position) + "-th planet in the solar system!")
print("{} is the {}-th planet in the solar system!".format(planet, position))
# 13.2. Decimal Points
pluto_mass = 1.303 * 10**22
earth_mass = 5.972 * 10**24
population = 52910390
print("Pluto weighs {:.2} kgrs ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(pluto_mass, pluto_mass / earth_mass, population))
# 13.3. Indexing
s = """
    - Pluto is a {0}!
    - No, it is a {1}....
    - I said it is a {0}!
    - No, it's a {1}!
    """.format('planet', 'dwarf planet')
print(s)

# 14. Dictionary
DICT = {planet : planet[0].upper() for planet in planets}
print(DICT, end='\n\n')
# 14.1. 1st for
for key in DICT:
    print(key, DICT[key], sep=" ---> ")
print()
# 14.2. 2nd for
for key in DICT.keys():
    print(key, DICT[key], sep=" ---> ")
print()
# 14.3. 3rd for
for key, value in zip(DICT.keys(), DICT.values()):
    print(key, value, sep=" ---> ")
print()
# 14.4. 4th for
for key, value in DICT.items():
    print(key, value, sep=" ---> ")
print()

# 15. Libraries - Modules
import math
help(math)
print(end='\n\n\n')
print("Type of math:", type(math))
print(end='\n\n\n')
print("Math contains:", dir(math))

# 16. Numpy
from numpy.random import randint as randi
dice_rolls = randi(low=1, high=7, size=100)
print("Dice rolls:", dice_rolls)
print("Type of dice rolls:", type(dice_rolls))
print("Mean =", dice_rolls.mean(), end='\n\n')

new_rolls = dice_rolls + 10
print("New rolls:", new_rolls)
print("Type of new rolls:", type(new_rolls))
print("Mean =", new_rolls.mean())

# 17. Arrays vs Lists
from numpy.random import randint as randi

# 17.1. Array (ndarray) to List
rolls = randi(low=1, high=7, size=20)
mean1 = rolls.mean()
print(type(rolls))
print(rolls, mean1, sep=' ---> ', end='\n\n')

# 17.2. Convert to list
rolls_list = rolls.tolist()
mean2 = sum(rolls_list) / len(rolls_list)
print(type(rolls_list))
print(rolls_list, mean2, sep=' ---> ')

# 18. Lists vs Arrays
from random import randrange as randr
import numpy

# 18.1. List
dice = [randr(1, 7) for i in range(20)]
mean1 = sum(dice) / len(dice)
print(type(dice))
print(dice, mean1, sep=' ---> ', end='\n\n')

# 18.2. Convert to array (ndarray)
dice_array = numpy.asarray(dice)
mean2 = dice_array.mean()
print(type(dice_array))
print(dice_array, mean2, sep=' ---> ', end='\n\n')

# 19. Array - Matrices
import numpy

L = list(range(1, 11))
M = [i**2 for i in L]
N = [i**3 for i in L]

# Lists in list
my_list = [L, M, N]
print("List:", my_list, sep=' ---> ', end='\n\n')
# Create array - matrix
my_array = numpy.asarray(my_list)
print("Array:", my_array, sep=' ---> ', end='\n\n')
# Access last element of 2nd row
last1 = my_list[1][-1]
last2 = my_array[1, -1]
print(last1, last1 == last2)

# 20. Variables and methods with double underscore (__)
print(dir(list))
print("__contains__" in dir(list), end='\n\n')

L = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = 21
print(x, L, sep='  ', end='\n\n')

print("x in L", x in L, sep=' ---> ')
print("This is happening, because the 'list' data type has the method named __contains__ and when I write the above message,")
print("the code executes this line of code:")
print("L.__contains__(x)", L.__contains__(x), sep=' ---> ')

# 21. Dropdown List
dropdown = 'Dog' #@param ["Cat", "Dog", "Cow", "Horse"]
print(dropdown)
