#topic
import pandas as pd

# -----------------------------------
# STEP 1: Load the dataset
# -----------------------------------
df = pd.read_csv("customer_orders.csv")

# -----------------------------------
# STEP 2: Print shape BEFORE cleaning
# -----------------------------------
print("Shape BEFORE cleaning:", df.shape)

# -----------------------------------
# STEP 3: Generate missing values report
# -----------------------------------
print("\nMissing Values Report:")
print(df.isna().sum())

# -----------------------------------
# STEP 4: Fill missing numeric values with median
# -----------------------------------
# Select only numeric columns
numeric_cols = df.select_dtypes(include=['number']).columns

# Fill missing values in numeric columns with median
for col in numeric_cols:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

# -----------------------------------
# STEP 5: Remove duplicate rows
# -----------------------------------
df = df.drop_duplicates()

# -----------------------------------
# STEP 6: Print shape AFTER cleaning
# -----------------------------------
print("\nShape AFTER cleaning:", df.shape)


