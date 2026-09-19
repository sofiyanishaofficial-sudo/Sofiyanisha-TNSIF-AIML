import pandas as pd

data = {
    "Name": ["Arun", "Bala", "Chitra", "Divya", "Kavin", "Meena", "Ravi", "Siva"],
    "Department": ["IT", "CSE", "ECE", "IT", "CSE", "ECE", "IT", "CSE"],
    "Marks": [85, 72, 90, 68, 78, 95, 81, 74],
    "Attendance": [85, 75, 92, 78, 88, 95, 79, 82]
}

df = pd.DataFrame(data)

print("First 5 Students:")
print(df.head())

average_marks = df["Marks"].mean()
print("\nAverage Marks:", average_marks)

print("\nStudents who scored more than 75:")
print(df[df["Marks"] > 75])

print("\nStudents whose attendance is below 80%:")
print(df[df["Attendance"] < 80])

print("\nStudents sorted based on marks:")
print(df.sort_values("Marks"))
