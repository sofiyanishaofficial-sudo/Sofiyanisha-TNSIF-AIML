import numpy as np

marks = np.array([85, 72, 90, 68, 78, 95, 81, 74, 88, 70])

total = np.sum(marks)

average = np.mean(marks)

highest = np.max(marks)

lowest = np.min(marks)

greater_than_75 = marks[marks > 75]

print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Marks greater than 75:", greater_than_75)
