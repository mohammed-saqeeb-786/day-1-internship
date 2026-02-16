#task 1
# Import required libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ---------------------------------
# Step 2: Label Encoding (Binary)
# ---------------------------------
label_encoder = LabelEncoder()

df['Transmission'] = label_encoder.fit_transform(df['Transmission'])

# Now:
# Automatic -> 0
# Manual -> 1
# (Order is assigned alphabetically by default)


# ---------------------------------
# Step 3: One-Hot Encoding (Nominal)
# ---------------------------------
df = pd.get_dummies(df, columns=['Color'], drop_first=True)

# drop_first=True removes one category
# This prevents Dummy Variable Trap (multicollinearity)


# -----------------------------
# Final Encoded Dataset
# -----------------------------
print("\nEncoded Dataset:")
print(df)



# task 2
# Import required libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# -----------------------------
# Step 1: Create Sample Dataset
# -----------------------------
data = {
    'Age': [22, 25, 47, 52, 46, 56, 48, 30, 34, 40],
    'Salary': [30000, 35000, 80000, 90000, 85000, 95000, 87000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# ---------------------------------
# Step 2: Standardization
# (Mean = 0, Std = 1)
# ---------------------------------
standard_scaler = StandardScaler()

df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data (Mean = 0, Std = 1):")
print(df_standardized)


# ---------------------------------
# Step 3: Normalization
# (Range 0 to 1)
# ---------------------------------
minmax_scaler = MinMaxScaler()

df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data (Range 0 to 1):")
print(df_normalized)




# task 3
# Import required libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# -----------------------------
# Step 1: Create Non-Linear Data
# -----------------------------
np.random.seed(42)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X + 5 + np.random.normal(0, 5, size=X.shape)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ---------------------------------
# Step 2: Linear Regression (Original Feature)
# ---------------------------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

r2_linear = r2_score(y_test, y_pred_linear)

print("R² score using Original Feature:", r2_linear)


# ---------------------------------
# Step 3: Polynomial Features (Degree = 2)
# ---------------------------------
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)

r2_poly = r2_score(y_test, y_pred_poly)

print("R² score using Polynomial Features (degree=2):", r2_poly)


# ---------------------------------
# Final Comparison
# ---------------------------------
if r2_poly > r2_linear:
    print("\nPolynomial features improved the model! ✅")
else:
    print("\nPolynomial features did not improve the model.")