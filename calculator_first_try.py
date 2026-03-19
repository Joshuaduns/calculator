import math


# from enum import Enum

# NOTE:This is storing the operations as strings. Giving them a literal?


# class Operation(Enum):
#     Add = "+"
#     Subtract = "-"
#     Multiply = "*"
#     Divide = "/"

Add = "+"
Subtract = "-"
Multiply = "*"
Divide = "/"


# NOTE:greeting but in all uppercase
greeting = " Welcome to Joshua's Calculator! ".upper()

print("")
# NOTE: was a testing to see if greeting would actually print
# print(greeting)

# NOTE:Greeting but centered inbetween a footer
print(greeting.center(50, "="))

print("\n\n")

# NOTE:This is for the usering putting the first number in the calculator
numberchoice1 = input("Please enter a number of your choice.")

print("\n\n")

# NOTE: below - This was a test to see if I can put the first number into a list
# firstnumber = list(numberchoice1)

# NOTE: The first number will be stored for later
firstnumber = numberchoice1

int(firstnumber)


# NOTE:This is asking the user what to do next with that number.
operation = input(
    "What do you want to do with this number?...\n+ for Add,\n- for Subtract,\n* for Multiply,\n\ for Divide\n")

user = str(operation)

print("\n\n")

numberchoice2 = input("Please enter the 2nd number of your choice.")

secondnumber = numberchoice2

int(secondnumber)

# NOTE: YOU NEED TO FIGURE OUT IF ELSE FOR THE OPERATION CHOICE

if user == "+":
    print("Hello fucker")


# print(numberchoice1)
