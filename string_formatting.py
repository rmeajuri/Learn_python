age = 26
age_as_str = str(age)
greeting = "You are, " + age_as_str
print(greeting)

spacing = """      
  
   
     
      
       """

print(spacing)

#or

age = 26
print(f"You are {age}") #Making use of the "f" string.

#or

name = "Rishab"
greeting = f"How are you, {name}"
print(greeting)

spacing = """      
  
   
     
      
       """
#or

name = "Rishab"
final_greeting = "How are you, {}?"
rishab_greeting = final_greeting.format(name)
print(rishab_greeting)

name = "Edmund"
edmund_greeting = final_greeting.format(name)
print(edmund_greeting)

#or

description = "{} is {} years old."
print(description.format("Bob", 26))

#or

description = "{} is {age} years old."
print(description.format("Bob", age=26))