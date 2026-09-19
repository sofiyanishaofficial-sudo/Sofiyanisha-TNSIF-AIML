from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

x = np.array([
    [20, 15000],
    [22, 18000],
    [25, 22000],
    [28, 30000],
    [30, 35000],
    [32, 40000],
    [35, 45000],
    [38, 50000],
    [40, 55000],
    [45, 60000]
])

y = np.array([0, 0, 0, 1, 1, 1, 1, 1, 1, 1])

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

logistic_model = LogisticRegression()
logistic_model.fit(x_train, y_train)

tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(x_train, y_train)

new_customer = [[27, 28000]]

logistic_prediction = logistic_model.predict(new_customer)
tree_prediction = tree_model.predict(new_customer)

print("Logistic Regression Prediction:", logistic_prediction[0])
print("Decision Tree Prediction:", tree_prediction[0])

logistic_test_prediction = logistic_model.predict(x_test)
tree_test_prediction = tree_model.predict(x_test)

logistic_accuracy = accuracy_score(y_test, logistic_test_prediction)
tree_accuracy = accuracy_score(y_test, tree_test_prediction)

print("Logistic Regression Accuracy:", logistic_accuracy)
print("Decision Tree Accuracy:", tree_accuracy)
