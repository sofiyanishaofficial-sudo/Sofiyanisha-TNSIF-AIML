from sklearn.ensemble import RandomForestClassifier
import numpy as np

x = np.array([
    [22, 2, 500],
    [25, 5, 600],
    [30, 1, 800],
    [35, 8, 550],
    [40, 10, 500],
    [28, 3, 900],
    [45, 12, 650],
    [32, 2, 850]
])


y = np.array([1, 0, 1, 0, 0, 1, 0, 1])

model = RandomForestClassifier()

model.fit(x, y)

prediction = model.predict([[30, 4, 700]])

if prediction[0] == 1:
    print("Churn: Leave")
else:
    print("Churn: Stay")
