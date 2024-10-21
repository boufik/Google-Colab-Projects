# Imports
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-whitegrid")
plt.rc("figure", autolayout=True)
plt.rc("axes", labelweight="bold", labelsize="large", titleweight="bold", titlesize=14, titlepad=10)



# AUXILIARY FUNCTIONS
def mean(l):
    return sum(l) / len(l)

def median(l):
    l.sort()
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        i1 = len(l) // 2
        i2 = i1 - 1
        return (l[i1] + l[i2]) / 2

def mode(l):

    d = {}
    for elem in l:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1

    max_freq = 0
    max_freq_list = []
    for elem in d:
        if d[elem] > max_freq:
            max_freq = d[elem]
    for elem in d:
        if d[elem] == max_freq:
            max_freq_list.append(elem)
    return max_freq, max_freq_list


def num_grades_between(low, high, grades):
    sum = 0
    for grade in grades:
        if low <= grade <= high:
            sum += 1
    return sum


def stats(grades):

    MEAN = mean(grades)
    MEDIAN = median(grades)
    times, MODES = mode(grades)
    print(f"Courses = {len(grades)}")
    print(f"   Mean = {MEAN:.2f}")
    print(f" Median = {MEDIAN:.2f}")
    print(f"   Mode = {MODES} ({times} times)")

    unique_grades = list(set(grades))
    unique_grades.sort()
    possible_grades = [elem / 2 for elem in range(10, 21)]
    d = {elem : 0 for elem in possible_grades}
    for grade in grades:
        d[grade] += 1

    print(f"\n   My unique grades = {unique_grades}")
    print(f"All possible grades = {possible_grades}\n\n---- Grades distribution ----")
    for key, value in d.items():
        print(f"{key} : {value} times")
    print("-----------------------------")
    return d


# MAIN FUNCTION
grades = [10, 9, 9.5, 8.5, 5, 7.5, 10, 10, 8.5, 8, 8.5, 10, 10, 9.5, 7.5, 10, 8.5, 6.5, 8, 8.5, 8, 7.5, 7, 9, 9, 8, 6, 10, 8, 6, 7.5, 8, 8, 8, 9.5, 9, 9.5, 9, 9, 8, 8.5, 10, 10, 10, 9.5, 6.5, 9.5, 9.5, 10]
# grades = grades + 6 * [10]        // Master's Thesis
d = stats(grades)
plt.bar(d.keys(), d.values(), align='edge', width=0.4)
plt.title("Grades distribution")
plt.xlabel("Grade")
plt.ylabel("Times")
plt.show()



# Plot the data
def cumulative(grades):
    possible_grades = [elem / 2 for elem in range(10, 21)]
    cumu =[]
    for possible_grade in possible_grades:
        value = num_grades_between(5, possible_grade, grades)
        cumu.append(value)
        print(f"Grades between 5.0 and {possible_grade}: {value} / {len(grades)}")
    print("\n")
    return possible_grades, cumu

poss, cumulative = cumulative(grades)
plt.plot(poss, cumulative)
plt.title("Cumulative distribution: Grades between 5.0 and 'Upper Bound'")
plt.xlabel("Upper Bound")
plt.ylabel("Grades")
plt.show()
