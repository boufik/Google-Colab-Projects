# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit



# AUXILIARY FUNCTIONS
# Example dictionary (3rd speed): {35:1600, 40:1800, 50:2200, 65:3000, 80:3800}
def define_speeds(dictionary, velocities, LEN):
    speed = ["-" for _ in range(LEN)]                                           # Data type = list with 21 entries (either "-" for NO DATA or some integer)
    keys = list(dictionary.keys())                                              # Example: keys = [35, 40, 50, 65, 80]
    for velocity in velocities:
        if velocity in keys:
            index = velocities.index(velocity)
            speed[index] = dictionary[velocity]
    return speed                                                                # Result speed = [-, -, -, -, -, -, 1600, 1800, -, 2200, -, -, 3000, -, -, 3800,  -, -, ......]



# 1. Create the 5 lists with velocities
velocities = list(range(5, 145, 5))
LEN = len(velocities)

dict1 = {15:1900, 20:2200, 25:2600, 30:3100, 35:3600}
dict2 = {20:1100, 30:1700, 40:2400, 50:3000, 55:3400}
dict3 = {35:1600, 40:1800, 50:2200, 65:3000, 80:3800}
dict4 = {60:2100, 65:2300, 80:2700, 85:3000, 90:3200, 100:3800}
dict5 = {70:1700, 80:2200, 85:2400, 90:2500, 100:2600, 120:3000, 140:4000}

speed1 = define_speeds(dict1, velocities, LEN)
speed2 = define_speeds(dict2, velocities, LEN)
speed3 = define_speeds(dict3, velocities, LEN)
speed4 = define_speeds(dict4, velocities, LEN)
speed5 = define_speeds(dict5, velocities, LEN)

# Create the speeds matrix (list with 5 lists) ---> convert it do a NumPy array ---> tranpose it
speeds_matrix = [speed1, speed2, speed3, speed4, speed5]
array = np.array(speeds_matrix)



# 2. Create the dataframe
columns = ["1st (rpm)", "2nd (rpm)", "3rd (rpm)", "4th (rpm)", "5th (rpm)"]
velocities_str = [f"{velocity:3d} km/h " for velocity in velocities]
df = pd.DataFrame(matrix, columns=columns, index=velocities_str)
print(df)



# 3. Filtering
# 3a. Filtering is needed in my lists, so I have to convert my lists into arrays
velocities = np.array(velocities)
speed1 = np.array(speed1)
speed2 = np.array(speed2)
speed3 = np.array(speed3)
speed4 = np.array(speed4)
speed5 = np.array(speed5)
# 3b. Filtering is applied in ARRAYS not LISTS ---> This way, "-" will not be displayed in next plots
condition1 = (speed1 != "-")
vel1 = velocities[condition1]
sp1 = speed1[condition1]
condition2 = (speed2 != "-")
vel2 = velocities[condition2]
sp2 = speed2[condition2]
condition3 = (speed3 != "-")
vel3 = velocities[condition3]
sp3 = speed3[condition3]
condition4 = (speed4 != "-")
vel4 = velocities[condition4]
sp4 = speed4[condition4]
condition5 = (speed5 != "-")
vel5 = velocities[condition5]
sp5 = speed5[condition5]
# 3c. Now, my lists are filtered, BUT the contain strings instead of integers
sp1 = [int(elem) for elem in sp1]
sp2 = [int(elem) for elem in sp2]
sp3 = [int(elem) for elem in sp3]
sp4 = [int(elem) for elem in sp4]
sp5 = [int(elem) for elem in sp5]
matrix = array.transpose()



# 4. Curve Fitting
def test_polynomial(x, p0, p1, p2, p3, p4):
    return p4*x**4 + p3*x**3 + p2*x**2 + p1*x + p0


def simulate(vel, sp, no_speed):

    print(100*"*")
    p_opt, p_cov = curve_fit(test_polynomial, vel, sp)
    p0, p1, p2, p3, p4 = p_opt
    x_model = np.linspace(min(vel), max(vel), 100)
    y_model = test_polynomial(x_model, p0, p1, p2, p3, p4)
    print("\n")

    print(f"f(x) = {p4:.2f}x^4 + {p3:.2f}x^3 + {p2:.2f}x^2 + {p1:.2f}x + {p0:.2f}")
    plt.scatter(vel, sp)
    plt.plot(x_model, y_model, 'r')
    sns.set_theme(style="darkgrid")
    plt.plot(vel, sp, 'bo')
    plt.title(f"----  Speed {no_speed} ----")
    plt.xlabel("Velocity (km/h)")
    plt.ylabel("Rotational Speed (rpm)")
    plt.show()
    print(100*"*", '\n')



# MAIN FUNCTION - RUN
vels = [vel1, vel2, vel3, vel4, vel5]
sps = [sp1, sp2, sp3, sp4, sp5]
no_speeds = [1, 2, 3, 4, 5]
for vel, sp, no_speed in zip(vels, sps, no_speeds):
    simulate(vel, sp, no_speed)
