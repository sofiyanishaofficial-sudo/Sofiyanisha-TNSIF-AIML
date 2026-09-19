import matplotlib.pyplot as plt

months = []
sales = []

for i in range(6):
    month = input("Enter month: ")
    sale = float(input("Enter sales amount: "))

    months.append(month)
    sales.append(sale)

plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.show()


plt.bar(months, sales, label="Monthly Sales")

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.show()
