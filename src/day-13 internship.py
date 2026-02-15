#topic
import pandas as pd

data ={
"Age": [25,30,35,40, 28, 32, 45, 50, 23, 36,29,41],
"Salary": [30000, 40000, 50000, 65000, 42000,48000, 80000, 90000, 28000, 52000, 46000, 70000],
"Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
"Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "Finance", "HR", "IT", "HR", "Finance"],
"Gender": ["M", "F", "M", "M", "F", "F", "M","M", "F","F", "M","F"]
}

df = pd.DataFrame(data)

#day 13 taks 👇
    
#TASK 1 : The Pattern Finder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample housing dataset
df = pd.read_excel("Housing.csv")

# 1. Histogram with KDE

sns.histplot(df["price"], kde=True)
plt.title("Distribution of Housing prices")
plt.xlabel("price")
plt.ylabel("Frequency")
plt.show()

# 2. Skewness and Kurtosis
print("Skewness:", df["price"].skew())
print("Kurtosis:", df["price"].kurt())

# 3. Count Plot for categorical column
sns.countplot(x="City", data=df)
plt.title("City Frequency")
plt.show()





#TASK 2: The Relationship Map
plt.subplot(1,2,1)
plt.scatter(x="area", y='price', data=df)
plt.title('Area vs Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df['furnishingstatus'],y=df['price'])
plt.xlabel('Furnishing Status')
plt.ylabel('Price')
plt.show()
plt.tight_layout()
print("AS FURNISHING STATUS INCREASES PRICE OF HOUSE ALSO INCREASES")





#TASK 3: The Pattern Finder
plt.subplot(1,2,1)
corr_matrix=df.corr(numeric_only=True)
print(corr_matrix)
print("There are no two variables with correlation score higher than 0.8")
sns.heatmap(corr_matrix,annot=True)
plt.show()
plt.subplot(1,2,2)
sns.boxplot(x=df ['price'])
plt.xlabel('Price')
plt.show()
plt.tight_layout()































