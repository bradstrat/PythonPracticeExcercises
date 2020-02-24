print('''Exercise 1: Create a program that asks user for their
name and age. Print out a message addressed to them that 
tells them the year that they will turn 100 years old.\n''')

#My answer is below...

def turn100(age):
     return ((2020 - age)+100)

def program():
     name = input("Hello New User!\nWhat is your name: ")
     print("\nHello {}! I will tell you when you will be 100...".format(name))
     age = int(input("What is your age in years: "))

     print("\nYou will turn 100 in the year {}".format(turn100(age)))

program()
          
