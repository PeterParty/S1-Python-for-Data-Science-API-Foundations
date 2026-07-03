import kagglehub
import numpy as np
import pandas as pd 
import tensorflow as tf
from tensorflow.keras import layers

print("TesnorFlow version:", tf.__version__)

# Download latest version
path = kagglehub.dataset_download("nikhil1e9/loan-default")
print(f"Path:{path}")
path = "C:\\Users\\Petrisor\\.cache\\kagglehub\\datasets\\nikhil1e9\\loan-default\\versions\\2\\Loan_default.csv"
print("Path to dataset files:", path)
loan_dataset= pd.read_csv(path)
print(f"Loan dataset columns:{loan_dataset.columns}")
# print(f"Loan dataset head 3:{loan_dataset.head(3)}")
x_train = loan_dataset[['Age', 'Income', 'LoanAmount', 'CreditScore']]
y_train = loan_dataset[['DTIRatio']]

print(f"x_train data:{x_train}")
print(f"y_train data:{y_train}")

loan_features = np.array(x_train)
loan_labels = np.array(y_train)

loan_model = tf.keras.Sequential([
    layers.Dense(64,activation='relu'),
    layers.Dense(1)
])

# loan_model.compile(loss=tf.keras.losses.MeanSquaredError(),optimizer = tf.keras.optimizers.Adam())

# loan_model.fit(loan_features,loan_labels,epochs=10)

normalize =layers.Normalization()

normalize.adapt(loan_features)

norm_loan_model =tf.keras.Sequential([
    normalize,
    layers.Dense(64,activation='relu'),
    layers.Dense(1)
])

norm_loan_model.compile(loss=tf.keras.losses.MeanSquaredError(),optimizer = tf.keras.optimizers.Adam())

norm_loan_model.fit(loan_features,loan_labels,epochs=10)

loan_probability_model = tf.keras.Sequential([
    loan_model,
    tf.keras.layers.Softmax()
])

norm_loan_probability_model = tf.keras.Sequential([
    norm_loan_model,
    tf.keras.layers.Softmax()
])
x_test = pd.DataFrame(
    {
        "Age":35,
        "Income":50000,
        "LoanAmount":10000,
        "CreditScore":680,
    }
)
x_test = x_test.to_numpy()
print("Loan probability model:",loan_probability_model(x_test))
print("Norm loan probability model:",norm_loan_probability_model(x_test))