# Imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)


# Each 1 of the first 2 dog years correspond for 10.5 human years
# The rest of dog years account for 4 human years
maxDogYears = 13
dogYears = list(range(maxDogYears + 1))
humanYears = [0] + 2 * [10.5] + (maxDogYears - 2) * [4]
print(humanYears)


# MAIN FUNCTION
humanYears = list(np.cumsum(humanYears))
print(f"Human years = {humanYears}\n")
plt.plot(dogYears, humanYears)
plt.xlabel("Dog Years")
plt.ylabel("Human Years")
plt.title("Dog Years vs Human Years")
plt.show()

# CURVE FITTING EXAMPLE
def poly1(x, a, b):
    return a * x + b

def fit_poly1(x, popt):
    x = np.array(x)
    a = popt[0]
    b = popt[1]
    return a * x + b

def poly1_2nd(x, a):
    return a * x

def fit_poly1_2nd(x, popt):
    x = np.array(x)
    a = popt[0]
    return a * x


def poly1_2nd(x, a):
    return a * x

def fit_poly1_2nd(x, popt):
    x = np.array(x)
    a = popt[0]
    return a * x

popt, pcov = curve_fit(poly1, dogYears, humanYears)
y = fit_poly1(dogYears, popt)
popt2, pcov2 = curve_fit(poly1_2nd, dogYears, humanYears)
y2 = fit_poly1_2nd(dogYears, popt)

STR1 = f"y = {popt[0]:.2f}x + {popt[1]:.2}"
STR2 = f"y = {popt2[0]:.2f}x"

print(f"Dog years = {dogYears}\nHuman Years = {humanYears}\nf(x) = ax + b\n")
plt.plot(dogYears, humanYears, 'blue')
plt.plot(dogYears, y, color='red')
plt.xlabel("Dog Years")
plt.ylabel("Human Years")
plt.title("Dog Years vs Human Years")
plt.legend(["Reality", "Curve Fitting: " + STR1])
plt.show()

print(f"\n\n\nDog years = {dogYears}\nHuman Years = {humanYears}\nf(x) = ax\n")
plt.plot(dogYears, humanYears, 'blue')
plt.plot(dogYears, y2, color='red')
plt.xlabel("Dog Years")
plt.ylabel("Human Years")
plt.title("Dog Years vs Human Years")
plt.legend(["Reality", "Curve Fitting: " + STR2])
plt.show()
