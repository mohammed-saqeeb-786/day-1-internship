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
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# 1. Create dummy data similar to your graph
data = {'Age': [19, 25, 28, 32, 35, 38, 43]}
df = pd.DataFrame(data)

# 2. Initialize the Scaler
scaler = StandardScaler()

# 3. Fit and transform the data
# We reshape because the scaler expects a 2D array
df['Age_Scaled'] = scaler.fit_transform(df[['Age']])

# 4. Plotting the 'Before' and 'After'
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Original Age (Similar to your uploaded image)
sns.histplot(df['Age'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Original Age Histogram')
axes[0].set_xlabel('Age (Raw Years)')

# Plot 2: Scaled Age
sns.histplot(df['Age_Scaled'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Scaled Age Histogram')
axes[1].set_xlabel('Age (Standardized Units)')

plt.tight_layout()
plt.show()

# Print values to see the difference
print("Original Values:\n", df['Age'].values)
print("\nScaled Values (Mean=0, Std=1):\n", df['Age_Scaled'].values)



# task 3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures,OneHotEncoder
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv("gdp.csv")
X_train,X_test,y_train,y_test = train_test_split(df[['Year']],df[['Value']],test_size=0.2,random_state=42)


model=LinearRegression()
model.fit(X_train,y_train)
baseline_pred=model.predict(X_test)
baseline_score=r2_score(y_test, baseline_pred)

print(baseline_score)


poly=PolynomialFeatures(degree=2,include_bias=False)

X_train_poly=poly.fit_transform(X_train)
X_test_poly=poly.transform(X_test)

poly_model=LinearRegression()
poly_model.fit(X_train_poly,y_train)
poly_pred=poly_model.predict(X_test_poly)
poly_score=r2_score(y_test, poly_pred)
print(poly_score)