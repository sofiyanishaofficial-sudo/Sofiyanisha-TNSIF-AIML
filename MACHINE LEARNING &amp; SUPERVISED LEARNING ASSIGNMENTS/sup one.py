from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([
    [20, 15000],
    [22, 18000],
    [25, 25000],
    [28, 30000],
    [30, 35000],
    [35, 40000],
    [40, 50000],
    [45, 60000]
])

y = np.array([0, 0, 0, 1, 1, 1, 1, 1])

model = LogisticRegression()

model.fit(x, y)

age = 32
income = 38000

prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Purchased: Yes")
else:
    print("Purchased: No")
