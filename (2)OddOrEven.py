print('''Ask the user for a number. Depending on whether the
number is even or odd, print out an appropriate message to the
user. Hint: how does an even / odd number react differently
when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.\n''')

#My answer is below...

def program():
     while True:
          data = {"number": None, "type": None}
          data["number"] = input("Please type a number: ")
          
          if int(data["number"])%4 == 0: data["type"] = "actually divisible by 4!"
          
          else:
               if int(data["number"])%2 == 0: data["type"] = "even"             
               if int(data["number"])%2 != 0: data["type"] = "odd"

          print("\nYour number, {num}, is {t}.\n".format(num = data["number"], t = data["type"]))

program()
               
