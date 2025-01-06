
# # What does Pandas stand for? 
# # Pandas stands for Python Data Analysis Library
# # What are the 2 collections used in Pandas?
# # Series and DataFrame
# # Name 4 things Pandas can do for us.
# # 1. Data Cleaning
# # 2. Data Transformation
# # 3. Data Visualization
# # 4. Data Analysis
# # To permanently sort a DataFrame, which keyword should one use with the df.sort() method?
# # ascending
# # What is a CSV?
# # CSV stands for Comma Separated Values
# # When cleaning data what values do we not like in our data?
# # missing values, duplicates, outliers, and inconsistent data

# Please Complete this Coding Exercise:
# Import NumPy, use one of the NumPy methods and create an array with a shape of (2, 3, 2). You can use the reshape method -- .reshape()

# Use NumPy .linspace() to create an array with 6 linearly spaced values between 0 and 20

# Make a Deep Copy of the above array 

# Concatenate these 3 arrays into a new array named 'newArray'...

#         ([[25, 16]])
#         ([[11, 2], [13, 4]])
#         ([[7, 81], [5, 6], [11, 12]])
# Sort 'newArray' in order into 'sortedArray'

# Unpack the array tuples from the above 'reshapedArray' into 4 well named variables. Print the 4 variables.

# Combined and sort the following arrays into one called 'comboArray' ...

#     one = ([10, 11, 12, 13, 14, 15, 16, 17])
#     two = ([20, 21, 22, 23, 24, 25, 26, 27])
#     three = ([ 0, 1, 2, 3, 4, 5, 6, 7])
# Take 'comboArray' and perform the following slicing activities:

# print sec1 - the 2nd element
# print sec2 - all elements from the 3rd element to the last
# print sec3 - all elements from the 4th to the 14th elements
# print sec4 - the last 6 elements
# print sec5 - all element from #0 up to and including #15, using the negative number method, i.e. taking a section from the end.
# print sec6 - from #20 every even element to the end
# print sec7 - from the last element moving forward, every 5th element.
# Using Series, create a DataFrame that looks like this:

# Ingredients	Quantity	Unit
# Flour	4	cups
# Milk	1	cup
# Eggs	2	large
# Spam	1	can
# Name: Dinner, dtype: object

# Take this data and create a DataFrame named studentData

#     {'Name': ['Jai', 'janusha', 'Gaurav', 'Anuj'],
#         'Height': [5.1, 6.2, 5.1, 5.2],
#         'Qualification': ['Msc', 'MA', 'Msc', 'Msc'],
#         'address': ['Delhi', 'Doha', 'Chennai', 'Dakhar'],
#         'Age': [21, 23, 24, 21],
#         'Pets': ['Dog', 'Bunny', 'Chinchilla', 'Parrot'],
#         'sport': ['Darts', 'Basketball', 'PaddleBoarding', 'Cricket']
#     }
# Add a new column to the DataFrame with the following deserts: ["ice cream", "Cashew Fudge", "waffels", "Carrot Halwa"]

# Sort the 'studentData' DataFrame in Ascending order -- Sorting by column 'Name' and then "address"

# Save this DataFrame here below to disc as a .CSV file with the name cows_and_goats.csv:

#     df = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
# (A) Using Pandas, make your own .CSV file with data on vegetables and save it. (B) Using Pandas, make a change to your CSV file, and save a copy with a different name.


# When done with homework:
# Due Date: The following Monday before class
# Make sure your homework file is well named
# Add the homework to your Homework repo
# Use git add ., git commit -m "message", and git push to upload your homework changes to GitHub in the cloud
# Create a JIRA ticket to indicate that your Homework is ready for review:
# In the "Summary" box: Include First Name and Last Initial, plus a short description in the Summary box (Ex: Jane D. Week # Homework Complete)
# In the "Description" box: Include GitHub repo url


# Final Note:
# Goal from this past week: - Expanded knowledge regarding NumPy - Understanding broadcasting - Introduction to Pandas - Knowledge and ability on how to upload documents using Pandas