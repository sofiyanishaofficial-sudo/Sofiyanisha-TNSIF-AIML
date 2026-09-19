import numpy as np

temperatures = np.array([28, 32, 31, 29, 34, 27, 33])

average = np.mean(temperatures)

highest = np.max(temperatures)

lowest = np.min(temperatures)

above_30 = temperatures[temperatures > 30]

updated_temperatures = temperatures + 2

print("Temperatures:", temperatures)
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print("Temperatures above 30°C:", above_30)
print("Updated Temperatures:", updated_temperatures)
