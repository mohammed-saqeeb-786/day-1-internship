import numpy as np

brr = np.array([1,2,3])
brr3 = np.array([10,10,10])
 
result = brr * brr3
print(result)

#topic 2
a = np.array([1,2,3,4,5])
a.shape 

b = np.array([[1,2],[3,4]])
b.shape
"reshaped"

arr = np.arange(12)
print(arr)
 
reshaped = np.reshape(arr,(3,4))
print(reshaped)

#task 1
import numpy as np

# For reproducibility (optional but nice for learning)
np.random.seed(42)

# 1. Create a 5x3 array of random integers between 50 and 100
scores = np.random.randint(50, 100, size=(5, 3))

# 2. Calculate the mean for each subject (column-wise mean)
subject_means = scores.mean(axis=0)

# 3. Subtract the mean from the original scores using broadcasting
centered_scores = scores - subject_means

# 4. Print results
print("Original Scores:")
print(scores)

print("\nSubject-wise Means:")
print(subject_means)

print("\nCentered Scores (After Broadcasting):")
print(centered_scores)

#task 2
import numpy as np

# 1. Create a 1D array with values 0 to 23
data = np.arange(24)

# 2. Reshape into a 3D array of shape (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)

# 3. Transpose to get shape (4, 2, 3)
final_data = reshaped_data.transpose(0, 2, 1)

# 4. Print the final shape and array
print( final_data.shape)
print(final_data)



