my_name = "Rishab"
your_name = input("Enter your name: ")
print(f"Hello {your_name}, my name is {my_name}")

#or Just to input an integer instead of a string

age = input("Enter your Age: ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")

#or to make the code a little easier

age = int(input("Enter your Age: "))
months = age * 12
print(f"You have lived for {months} months.")