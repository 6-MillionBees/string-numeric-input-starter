# Arden Boettcher
# 9/13/24
# string numeric input starter main


# Task 1
# Use the input( ) function to prompt the user to enter his/her first name and the name of the program they attend at Career Tech.
# Assign the user's responses to variables
# Use concatenation to build an output string that displays the user's answers
# Please use correct capitalization, spelling, and punctuation in your code

user_name = input('Please enter your first name: ')
career = input('What program do you attend in Career Tech? ')

print('Hi ' + user_name.title() + '! Welcome to Career Tech! I hope you have fun learning in ' + career.title())

# Task 2
# prompt the user to enter their current age
# Assign their response to a variable age
# On the next line of code, use the int( ) function to convert the user's response to an integer (a number that doesn't have a decimal point)
# Display a sentence that contains the user's current age
# Challenge: Have Python add 10 years to the user's current age; then display a sentence that says what the user's age will be ten years from now

age = float(input('how old are you? '))
age10 = int(age) + 10

if age == 1:
    print(f'You are {int(age)} year old. How are you writing this?') # I felt like making the grammar proper, you can't be saying years if it isn't plural
elif age < 1:
    print(f'You are a baby. How are you writing this?!') # it did make it overly complicated though
else: 
    print(f'You are {int(age)} years old') # like making input a float only to make it an integer later?

print(f'and you will be {age10} years old in 10 years')

# Task 3
# Using the input( ) and int ( ) functions in a single line of code, prompt the user to enter the number of people in his/her family
# Use concatenation to display a sentence that says how many people are in the user's immediate family
# HINT: The Python str(  ) function might come in handy here!
# On the next line of code, use an f-string to display a sentence that says how many people are in the user's immediate family

family = int(input('how many people do you have in your family? '))

print('you have ' + str(family) + ' people in your family')

print(f'you have {family} people in your family')

# Task 4
# Using the input( ) and float ( ) functions in a single line of code, prompt the user to enter their height in inches (so 60 for 5'10" tall)
# Write a formula that tells Python how to do the math to convert inches into centimeters
# HINT: Define a constant called CONVERSION_FACTOR and assign it the value 2.54
# Use concatenation to display a sentence that says how tall the user is in inches AND in centimeters
# HINT: The Python str(  ) function might come in handy here!
# Also show you know how to use an f-string to display the user's height in both inches and centimeters

def heightfunc():
    height = float(input('Please enter your hight in inches: '))
    CONVERSION_FACTOR = 2.54
    cm_height = height * CONVERSION_FACTOR
    print(f'you are {height} inches tall and {cm_height} centimeters tall!')

heightfunc()

# Task 5
# Comment
# Comment
