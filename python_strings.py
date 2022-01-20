my_string = "Hello, world"
print(my_string)

multiline = """Hello world.


My name is Rishab. Welcome to my program.
"""
print(multiline)

#Adding strings

name = "Rishab"
greeting = "Hello, " + name
print(greeting)

#We cannot add an integer and a string. The integer has to be converted to a string and then needs to be added.

age = "26"
greeting = "You are, " + age
print(greeting)

#or

age = 26
age_as_str = str(age)
greeting = "You are, " + age_as_str
print(greeting)