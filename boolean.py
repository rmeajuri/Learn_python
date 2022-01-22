print("This is a sample to test the functionality of boolean operators in python as follows: ")
truth = True
false = False

##### General Boolean checks

age = 20
is_over_age = age >= 18
print(is_over_age)
is_over_age = age < 18
print(is_over_age)

##### Using boolean operators in a condition check (if/else loop)

my_number = 10
your_number = int(input("Enter a number, we will check to see if it matches with the records: "))

match_check = my_number == your_number
if match_check:
  print(f"The number provided by you matches our number: {match_check}")
else:
  print("The number entered by you doesn't match our number in the records. Thanks for your time. Bye..!")