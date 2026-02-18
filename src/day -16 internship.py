#task 1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

#Generate Datasets
# Normal Distribution with (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Incomes)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Exam Test Scores)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Convert to Pandas DataFrame
data = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})
# 2️⃣ Plot Histograms with KDE

plt.figure(figsize=(18, 5))

# Heights (Normal)
plt.subplot(1, 3, 1)
sns.histplot(data["Heights"], kde=True)
plt.title("Human Heights (Normal Distribution)")

# Incomes (Right-Skewed)
plt.subplot(1, 3, 2)
sns.histplot(data["Incomes"], kde=True)
plt.title("Household Incomes (Right-Skewed)")

# Scores (Left-Skewed)
plt.subplot(1, 3, 3)
sns.histplot(data["Scores"], kde=True)
plt.title("Test Scores (Left-Skewed)")

plt.tight_layout()
plt.show()

# 3️⃣ Compare Mean and Median

datasets = ["Heights", "Incomes", "Scores"]

for col in datasets:
    mean = data[col].mean()
    median = data[col].median()
    
    print(f"\n{col}")
    print(f"Mean   : {mean:.2f}")
    print(f"Median : {median:.2f}")
    
    if mean > median:
        print("Distribution is Right-Skewed")
    elif mean < median:
        print("Distribution is Left-Skewed")
    else:
        print("Distribution is Approximately Normal (Symmetric)")
        
        
#task 2        
import pandas as pd
import numpy as np

# STEP 0: Create Your Dataset
data = {
    "value": [50, 52, 49, 51, 48, 200, 47, 53, 46, 54]
}


df = pd.DataFrame(data)


# STEP 1: Calculate Mean 
mean = df["value"].mean()

# STEP 2: Calculate Standard Deviation 
std_dev = df["value"].std()

# STEP 3: Calculate Z-Score here is the formula
# Z = (x - μ) / σ
df["z_score"] = (df["value"] - mean) / std_dev

# STEP 4: Identify Outliers all
# |Z| > 3
outliers = df[np.abs(df["z_score"]) > 3]

# OUTPUT RESULTS
print("Mean (μ):", mean)
print("Standard Deviation (σ):", std_dev)

print("\nDataset with Z-Scores:")
print(df)

print("\nStatistical Outliers (|Z| > 3):")
print(outliers)


#task 3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# 1️ Create a heavily right-skewed dataset (like income)
population = np.random.exponential(scale=50000, size=100000)

# Take 1000 samples of size 30 and compute their means
sample_means = []

for _ in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

# Plot Original Data vs Distribution of Sample Means
plt.figure(figsize=(14, 5))

# Original skewed population
plt.subplot(1, 2, 1)
sns.histplot(population, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.xlabel("Income")

# Distribution of sample means
plt.subplot(1, 2, 2)
sns.histplot(sample_means, kde=True)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Means")

plt.tight_layout()
plt.show()

# 4️ Print  insight comparison statistics
print("Population Mean:", np.mean(population))
print("Mean of Sample Means:", np.mean(sample_means))
print("Population Std Dev:", np.std(population))
print("Std Dev of Sample Means:", np.std(sample_means))




