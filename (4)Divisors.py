print('''Create a program that asks the user
for a number and then prints out a list of all
the divisors of that number. (If you don’t
know what a divisor is, it is a number that
divides evenly into another number. For example,
13 is a divisor of 26 because 26  13 has no
remainder.)\n''')

#timing is a module that times the execution of a program
import timing

#My answer is below...

# 402653184


length = int(input("Type a number: "))

divisors = []

for number in range(1, length):
     if length%number == 0:
          divisors.append(number)

print(divisors)

timing.endlog()
input()





