from sklearn.tree import DecisionTreeClassifier
import numpy as np

x = np.array([
    [0, 0],
    [0, 1],
    [1, 1],
    [1, 0],
    [2, 0],
    [2, 1],
    [0, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 0, 1, 1, 0, 1])

model = DecisionTreeClassifier()

model.fit(x, y)

prediction = model.predict([[0, 1]])

if prediction[0] == 1:
    print("Play: Yes")
else:
    print("Play: No")
