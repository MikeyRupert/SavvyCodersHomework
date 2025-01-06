# week 3 homework

# What is an algorithm?
# a list of things to do in a specific order to accomplish a goal or automate a thing

# Variable names may not start with certain characters - name two.
# &&&and $, 
# $ = 1
# %=1 

# What is a Semantic error?
#  when we screw up typing or something is not defined correctly usually small spelling error, usually when we try to add but subtract 

# What is the #1 rule of coding / debugging?
# always have a plan, when in doubt pinky out

# List 5 Python reserved words.
# andbreak, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield, with

# Multi-line string with name, food, and dream job

bio = """Mike 
Steak
Scientist"""

# data types

sailor_name = "Popeye"  # string
popeye_pie_age = 42         # integer
popeye_pie_height = 6.14     # float
spinach = False     # boolean
popeye_pie_list_str = ["Popeye", "Spinach", "Pie"]   # list

print(len(sailor_name))

print(sailor_name[3])
savvy = "Learning Data Analytics and Python is Awesome!"

print(savvy[5:24])  

savvy = savvy.replace("Awesome", "great")

"Python" in savvy

name, age, length = "Mike", 31, "6ft"

miniBio = f"Hi my name is {name}, I am {length} and {age} yrs old today."

print(miniBio)

print(float(age))

#  lists = [element]

mixed_list = ["Python", 42, 3.14, True, [1, 2, 3]]

mixed_list[1] = "monkey"

mixed_list.append("something to end")
mixed_list.insert(0, "something to start")

print(len(mixed_list))

second_list = mixed_list[2:5]
print(second_list)

mixed_list.extend(second_list)

simList = [1, 5, 2, 4, 3]

simList.sort()
print(simList)

third_list = simList.copy()

fourth_list = second_list + third_list

#  tuples = (element)

first_tuple = (1, 10.2, 3.14, 30, 10)
print(type(first_tuple))

second_tuple = first_tuple * 3

print(second_tuple[11])

sorted_tuple = sorted(second_tuple)
print(sorted_tuple)

third_tuple = sorted_tuple[0:4]

one, two, three, four = third_tuple
print(one, two, three, four)

fourth_tuple = (50,)
print(fourth_tuple)

fifth_tuple = second_tuple + tuple(third_tuple)
print(fifth_tuple)

#  sets = {element}

first_set = {1, 2, 3}
fruits = ["apple", "banana", "orange"]
first_set.update(fruits)
print(first_set)
first_set.add("car")

second_set = {"book", "phone", "laptop"}

third_set = first_set.union(second_set)

second_set.pop()
print(second_set)

first_set.clear()
print(first_set)

third_set.discard("car")
third_set.remove(3)
print(third_set)

# dict = {key: value}

my_dict = {
    "name": "ricky balboa",
    "age": 31,
    "height": 6.14,
    "is_student": True,
    "hobbies": ["reading", "coding"]
}

print(my_dict["age"])

my_dict["name"] = "Mike"

my_dict["color"] = "blue"

my_dict["numbers"] = (1, 2, 3)

print(list(my_dict.keys()))
print(list(my_dict.values()))

second_dict = my_dict.copy()

second_dict.pop("age")
print(second_dict)

empty_dict = second_dict.clear()
print(empty_dict)
