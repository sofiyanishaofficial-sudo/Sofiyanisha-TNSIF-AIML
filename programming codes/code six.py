import matplotlib.pyplot as plt

students = ["Arun", "Bala", "Chitra", "Divya", "Kavin",
            "Meena", "Ravi", "Siva", "Priya", "Rahul"]

marks = [85, 72, 90, 55, 38, 95, 68, 45, 78, 32]

plt.bar(students, marks)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=45)

plt.show()



excellent = 0
good = 0
average = 0
needs_improvement = 0

for mark in marks:
    if mark >= 80:
        excellent += 1
    elif mark >= 60:
        good += 1
    elif mark >= 40:
        average += 1
    else:
        needs_improvement += 1

categories = ["Excellent", "Good", "Average", "Needs Improvement"]
students_count = [excellent, good, average, needs_improvement]

plt.pie(students_count, labels=categories, autopct="%1.1f%%")

plt.title("Student Performance Distribution")

plt.show()
