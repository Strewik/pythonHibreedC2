# def FunctionName(args):
#     '''docstring'''
#     function-body


# function declaration

def greet(name):
    """A funtion to greet a user"""
    print('Hello, ' + name + '. How are you?')
    
# function calling/ invoking a function
greet("John Doe")
greet('Elijah')
greet('Person')

def absolute_value(num):
    if num >= 0:
        return "Absolute number"
    else:
        return "not absolute number"
    
# print(absolute_value(5))
print(absolute_value(-5))

def tax(income, tax_percentage):
    total_tax = income * tax_percentage
    return total_tax

print(tax(5000, 0.4)) 