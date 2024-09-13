
# String & Numeric Input in Python

## Submitting Your Work

- Add Mr. Provencher as a collaborator to your repository
- My Career Tech email address: bprovencher@northwested.org
- Watch this video about how to [add a collaborator](https://youtu.be/6RTCsFqzfcY?feature=shared&t=30) to an online GitHub repository

## Getting Started

- Submit the URL that points to your repo on Google Classroom
- Complete the stations for this lesson
- Create a **public** GitHub repo named: **string-numeric-input-practice**
- Add a `main.py` file to your repository
- Write the code for this station in your `main.py` file 

## Resources

- Review these two resources before you attempt to complete Station 6
  - [Bro Code: Python User Input](https://www.youtube.com/watch?v=DB9Cq6TSTuQ&authuser=0)
  - [How to declare (create) a CONSTANT in Python](https://www.toppr.com/guides/python/python-introduction/variables-constants-literals/python-variables-constants-and-literals/)

## General Specifications

- Add a comment block to the top of your Python script, like so:
```python
# Abraham Lincoln
# 24 MAR 20XX
# String & Numeric Input
```
- Use short, descriptive variable names
- Write your variable names in lowercase

## Programming Practice

In your `main.py` file, write the following code:

### Task 1
- Use the `input( )` function to prompt the user to enter his/her first name and the name of the program they attend at Career Tech.
- Assign the user's responses to variables
- Use concatenation to build an output string that displays the user's answers
- Please use correct capitalization, spelling, and punctuation in your code

### Task 2
- On one line, prompt the user to enter their current age
- Assign their response to a variable `age`
- On the next line of code, use the `int( )` function to convert the user's response to an **integer** (a number that doesn't have a decimal point)
- Display a sentence that contains the user's current age
- Challenge: Have Python add 10 years to the user's current age; then display a sentence that says what the user's age will be ten years from now

### Task 3
- Using the `input( )` and `int ( )` functions in a single line of code, prompt the user to enter the number of people in his/her family
- Use **concatenation** to display a sentence that says how many people are in the user's immediate family
    - HINT: The Python `str(  )` function might come in handy here!
- On the next line of code, use an f-string to display a sentence that says how many people are in the user's immediate family

### Task 4
- Using the `input( )` and `float ( )` functions in a single line of code, prompt the user to enter their height in inches (so **60** for 5'10" tall)
- Write a formula that tells Python how to do the math to convert inches into centimeters
   - HINT: Define a constant called CONVERSION_FACTOR and assign it the value 2.54
- Use **concatenation** to display a sentence that says how tall the user is in inches AND in centimeters
    - HINT: The Python `str(  )` function might come in handy here!
- Also show you know how to use an f-string to display the user's height in both inches and centimeters
