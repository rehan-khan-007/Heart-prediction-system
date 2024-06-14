import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

# Function to load and prepare the data
def load_and_prepare_data(file_path):
    heart_data = pd.read_csv(file_path)
    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']
    return X, Y

# Function to scale data
def scale_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, scaler

# Function to split data
def split_data(X, Y):
    return train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Function to train model
def train_model(X_train, Y_train):
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, Y_train)
    return model

# Function to evaluate model
def evaluate_model(model, X_train, Y_train, X_test, Y_test):
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
    print('Accuracy on Training data : ', training_data_accuracy)

    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
    print('Accuracy on Test data : ', test_data_accuracy)

    # Calculate and print additional metrics
    precision = precision_score(Y_test, X_test_prediction)
    recall = recall_score(Y_test, X_test_prediction)
    f1 = f1_score(Y_test, X_test_prediction)
    
    print('Precision on Test data : ', precision)
    print('Recall on Test data : ', recall)
    print('F1 Score on Test data : ', f1)

# Function to make predictions
def make_prediction(model, scaler, input_data, feature_names):
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    input_data_df = pd.DataFrame(input_data_as_numpy_array, columns=feature_names)
    input_data_scaled = scaler.transform(input_data_df)
    prediction = model.predict(input_data_scaled)
    return prediction[0]
