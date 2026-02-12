#task 1
import pandas as pd
import numpy as np

#Starts creating a dictionary to store the dataset and clean it.
data = {
    "student_id": [1, 1, 3, 4, 5, 6, 1],
    "name": ["asif", "dalal", None, np.nan, "asif", "pig", "asif"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad", "bangalore"]
}

#Converts the dictionary into a Pandas DataFrame with the help of pd
df = pd.DataFrame(data)
s
print("Shape and BEFORE cleaning:", df.shape)

#Prints a title for missing value report.
print("Missing Values")
print(df.isna().sum())

numeric_columns = df.select_dtypes(include=['number']).columns

for col in numeric_columns:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows found in this:", duplicate_count)

df = df.drop_duplicates()

print("\nShape AFTER cleaning data:", df.shape)

print("\nData cleaning completed successfully!")

#task 2
import pandas as pd
import numpy as np

data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "name": ["asif", "dalal", None, np.nan, "asif", "pig"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad"],
    "Price": ["$100", "$250", "$175", "$300", "$400", "$150"],
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05", "2024-05-12", "2024-06-20"]
}

df = pd.DataFrame(data)

print("Initial Data Types:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData Types After Conversion:")
print(df.dtypes)

print("\nUpdated DataFrame:")
print(df)


# task 3
import pandas as pd
import numpy as np

data = {
    "student_id": [1, 1, 3, 4, 5, 6],
    "name": ["Asif", "dalal", "hyderabad", "asif", "pig", "asif"],
    "city": [" bangalore", "GULBARGA", "gurgaon", "wadi ", "SHABAD", "Bangalore"]
}

df = pd.DataFrame(data)

print("Before Cleaning:")
print(df["city"].unique())

df["city"] = df["city"].str.strip()
df["city"] = df["city"].str.title()

print("\nAfter Cleaning:")
print(df["city"].unique())


