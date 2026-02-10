#funtion adding
def add(a,b):
    print(a+b)
    
result = add(2, 4)
print(result)    

#funtion normal
def show():
    print("me your talent")
    
show()  

#global and local
x=10

def show_value():
    x=5
    print(x)
    
show_value()

print(x)

#topic 4

import math
import random

print(math.sqrt(3))
print(random.randint(55, 65))

from math import sqrt
print(math.sqrt(50))



# this is the funtion which is adding the numbers
#topic 3
count = 0

def add():
    global count
    count+=1
    
add()
print(count)



#task 1
def calc_rectangle(length, width):
    area=length*width
    perimeter=2*(length+width)
    return area, perimeter

#Calling the function
calc_rectangle(3, 4)

#input of length and width
length=int(input("Enter the length:"))
width=int(input("Enter the breadth:"))

#assigning the variables
area, perimeter = calc_rectangle(length, width)

#Printing the value
print(f"The area of rectangle is {perimeter}")
print(f"The ar----ea of rectangle is {area}")

#task 2

# Utility functions (normally in math_operations.py)
def power(base, exp):
    return base ** exp


def average(numbers_list):
    return sum(numbers_list) / len(numbers_list)


# Main execution (normally in main.py)
result_power = power(2, 10)
numbers = [10, 20, 30, 40]
result_average = average(numbers)

print(f"2^10 = {result_power}")
print(f"Average = {result_average}")

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












    