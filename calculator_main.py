
greeting = " Welcome to Joshua's Calculator! ".upper()

print("")

print(greeting.center(50, "="))

print("\n\n")

numberchoice1 = input("Please put in the first number: ")

operation = input(
    "What do you want to do with this number?...\n+ for Add,\n- for Subtract,\n* for Multiply,\n/ for Divide\n")


numberchoice2 = input("Please put in the second number: ")

# sumresultadd = int(numberchoice1) + int(numberchoice2)
# sumresultsubtract = int(numberchoice1) - int(numberchoice2)
# sumresultmultiply = int(numberchoice1) * int(numberchoice2)
# sumresultdivide = int(numberchoice1) / int(numberchoice2)

user = operation

if user == "+":
    print("The sum is:", float(numberchoice1) + float(numberchoice2))
elif user == "-":
    print("The sum is", float(numberchoice1) - float(numberchoice2))
elif user == "*":
    print("The sum is", float(numberchoice1) * float(numberchoice2))
elif user == "/":
    print("The sum is", float(numberchoice1) / float(numberchoice2))
