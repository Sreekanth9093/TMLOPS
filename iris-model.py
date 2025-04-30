import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
import pickle

# Reading the data
iris = pd.read_csv("data/iris.csv")
print(iris.head())
print(iris.columns)

iris_data = load_iris()
iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris['species'] = iris_data.target

# Use the correct column names
x = iris[iris_data.feature_names]
y = iris['species']


#y = iris['species']
#iris.drop(columns='species', inplace=True)
#x = iris[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]

# Training the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = LogisticRegression(max_iter=100)
model.fit(x_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))