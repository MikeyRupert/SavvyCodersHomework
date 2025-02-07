# %%
# What does one need to do to use a module?
# its important to import the stuff we need from the module

# %%
# Name a Module (not the DateTime Nodule) we looked at and write a line or 2 of code as an example using this module.
import math
print(math.sqrt(16))
import torch
x = torch.tensor([1,2,3])
y = torch.tensor([3,2,1])
result = x @ y
result
# %%
# What is a benefit of using Exception handling?
try:
    print(1/0)
except ZeroDivisionError:
    print("cant divide by zero guy")
    
#  this is a complicated but way to handle errors that may happen in our code like passing a string to a function that expects an integer
# %%
# what are the 4 components used for Python Exception Handling?
# try, except, else, finally
# %%
# NumPy arrays are like what Python data type?
# NumPy arrays are like lists but they are more efficient for certain operations like math
# %%
# What is one of the main benefits of using NumPy arrays.
# NumPy arrays are more efficient for certain operations like math, easier to use for graphs and quickly looking data thanks to modules 
# %%
# What is one of the main requirements about the 'dtype' of NumPy arrays?
# numpy tries to make all elements in the array the same datatype of arry

# %%
# Of the 10 uses of NumPy, name 2. make array and convert to float
import numpy as np
x = np.array([1,2,3])
print(x)
w = np.array([1,2,3], dtype=float)
print(w)
# %%
# Name one of the other libraries we'll use with NumPy?
import pandas as pd
# %%
# What is the shape of NumPy arrays?
# the shape of a NumPy array is the number of rows and columns in the array
x = np.array([[1,2,3],[4,5,6]])
print(x.shape)
# %%
# What is a Tensor?
# a tensor is a multi-dimensional array
import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6]]).float()
w = torch.rand(3, 2).float()
result = x @ w
w.shape
x.shape
result.shape
print(result)
# %%
# Name a reason why it's better using NumPy for Data Analysis than using a Python List?
# NumPy arrays are more efficient for certain operations like math, easier to use for graphs and quickly looking data thanks to modules 
#  its faster and built to handle large data sets
# %%
# When creating an "empty" array, where do the elements come from?
# the elements come from the memory of the computer
# %%

# Flow Control Methods:
# Create an if statement: if 'age' is greater than or equal to 25, print "Renting a car is more affordable", however if 'age' is less than 25, print "Renting a car is very expensive."
# %%
# Create and chain an if-else statement: if 'age' is greater than or equal to 25, print "Renting a car is more affordable." If 'age' is less than 25 but greater than or equal to 18, print "Renting a car is very expensive." Finally, if age is less than 18, print "You cannot legally rent a car."
# %%
# Loop over the following string to (1) count all the characters in the string and (2) print out all the vowels -- "The quick brown fox jumps over the lazy dog"
# %%
# Write a nested loop that prints out every piece of clothing from the couture list, in every fashionable color from the panettone set: couture = ["trousers", "blouse", "bandana", "cumber band", "blazer", "vest", "french beret", "scarf", "stole"] and panettone = {"cerise", "fuchsia", "aqua", "maple", "auburn", "burnt sienna", "gunmetal blue", "Dark Sapphire"}
# %%
# Use range as a loop to calculate the sum of all the numbers from 1 to 100
# %%

# Print the second item in this fruits list. ["apple", "banana", "cherry"]
# %%
# Change the value from "apple" to "kiwi", in the fruits list. ["apple", "banana", "cherry"]
# %%
# Use the append method to add "orange" to the fruits list. ["apple", "banana", "cherry"]
# %%
# Use the insert method to add "lemon" as the second item in the fruits list. ["apple", "banana", "cherry"]
# %%
# Use the remove method to remove "banana" from the fruits list. ["apple", "banana", "cherry"]
# %%
# Use negative indexing to print the 3rd and 2nd to last items in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# %%
# Use a range of indexes to print the third, fourth, and fifth item in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# %%
# Use the correct syntax to print the number of items in the list. ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# %%
# Use the correct syntax to sort this list in reverse order ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# %%

# Use a Python code file for this section:

# Use the DateTime module to get Current Date and Time, and save it to a variable. Then extract just the Full month name form that variable.
# %%

# Write a simple function that takes 2 parameters -- a first name and a day name.
# %%
# Set a default value for the day name of Sunday.
# %%
# Have the function print out a greeting -- using the parameters -- that says something like "Hi first-name! Happy day-name!". Remember to use the variables in the greeting to replace first-name and day-name.
# %%
# Invoke this function with 2 variables.
# %%
# Invoke this function with 1 variable only.
# %%
# Write a block of code to handle one of the most common Python exception errors. Select one of the common errors from the curriculum section on Python Exception handling. Have your code example uses the try,except, else, and finally components.
# %%


# When done with homework:
# Due Date: The following Monday before class
# Make sure your homework file is well named
# Add the homework to your Homework repo
# Use git add ., git commit -m "message", and git push to upload your homework changes to GitHub in the cloud
# Create a JIRA ticket to indicate that your Homework is ready for review:
# In the "Summary" box: Include First Name and Last Initial, plus a short description in the Summary box (Ex: Jane D. Week # Homework Complete)
# In the "Description" box: Include GitHub repo url
# %%
