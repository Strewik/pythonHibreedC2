# datatypes

# numbers

# integers
num1 = 3
num2 = -4

# float numbers
num3 = 3.14

# complex numbers
num4 = 1+2j

print("========================================")

a = 5.5
print(a, "is of type", type(a))


# Character

letter = 'a'

# Strings
# String is sequence of Unicode characters. We can use single 
# quotes or double quotes to represent strings. 
# Multi-line strings can be denoted using triple 
# quotes, ''' or """.

month = "October 15 - 2022 #&^*)"
day = 'Saturday'

# ()- parentheses
# [] - square brackets
# {} - braces

print("========================================")

# list datatype
elements = [1, 2.2, 'python']
print(elements)
      #  0 1  2  3  4  5   6  7 index
marks = [5,10,15,20,25,30,35,40]
# mutated element in position 1
marks[1] = 999
print(marks[1])
print(marks[0:4])


print("========================================")

# tuple

age = (12, 34, 56, 45, 32)
age[1] = 45
print(age[1])

#set
# Set is an unordered collection of unique items. 
# Set is defined by values separated by comma inside 
# braces { }. Items in a set are not ordered.

position = {5, 6, 3, 1, 12,}
names = {"anna", "john", "doe", "jane", 22, 45}

# Dictionary
# Dictionary is an unordered collection of key-value pairs.
# It is generally used when we have a huge amount of data. 
# Dictionaries are optimized for retrieving data. 
# We must know the key to retrieve the value.

dictionary = {"key":'value',  'key':2}
student1 = {"name": "John", "age":50, "Class":"python"}
student2 = {"name": "jane", "age":20, "Class":"python"}



