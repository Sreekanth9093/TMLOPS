# Import necessary libraries
import numpy as np  # For numerical computations
import pandas as pd  # For data manipulation and analysis
from sklearn.linear_model import LinearRegression  # For linear regression model
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
import pickle  # For saving and loading the trained model
import os  # For file and directory operations

# Check if the required directories exist, if not create them
# This ensures the 'model' directory exists to save the trained model
if not os.path.exists('model'):
    os.makedirs('model')

# Define the path to the dataset
data_path = 'data/rental_1000.csv'

# Load the dataset into a pandas DataFrame
df = pd.read_csv(data_path)

# Feature engineering: Select Features (X) and Label (y)
# 'rooms' and 'area' are the input features, and 'price' is the target variable
X = df[['rooms', 'sqft']].values  # Extract feature columns as a NumPy array
y = df['price'].values  # Extract the target column as a NumPy array

# Split the dataset into training and testing sets
# 80% of the data is used for training, and 20% is used for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate a Linear Regression model
lr = LinearRegression()  # Initialize the Linear Regression model
lr_model = lr.fit(X_train, y_train)  # Train the model on the training data
lr_score = lr.score(X_test, y_test)  # Calculate the R^2 score on the test data
lr_rmse = np.sqrt(np.mean((lr.predict(X_test) - y_test) ** 2))  # Calculate the Root Mean Squared Error (RMSE)
print(f"Linear Regression - R^2 Score: {lr_score:.4f}, RMSE: {lr_rmse:.4f}")

# Save the trained Linear Regression model to a file
# The model is saved as a pickle file in the 'model' directory
model = lr_model  # Assign the trained model to a variable
model_path = 'model/model.pkl'  # Define the path to save the model
with open(model_path, 'wb') as file:
    pickle.dump(model, file)  # Save the model using pickle

# Print a success message indicating the model has been saved
print(f"Model saved successfully at {model_path}!")