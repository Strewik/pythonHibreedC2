# if condition:
#     if-body/statements
# elif condition:
#   elif-body/statements
# else:
    # else-body
  
from cgitb import small


age = 123
  
if age < 18:
    print("You are not allowed to bet")
else:
    print("You are allowed to bet")
    
    
num = 0

if num > 0:
    print("Num is a positive number")
elif num == 0:
    print("Num is 0")
else:
    print("Num is negative")
    

size = 6

if size >= 1 and size =< 2:
    print("small")
    # True          False
elif size >= 3 and size <=5:
    medium
    # true         true
elif size >= 6 and size <= 9:
    large
else: print("We don't have that size")
