# Program to display the Fibonacci sequence


number = int(input("How many Fibonacci numbers? "))

# first two terms
x, y = 0, 1
count = 0

# check if the number of terms is valid
if number <= 0:
   print("Please enter a positive number:-")
elif number == 1:
   print("Fibonacci sequence upto",number,":-")
   print(n1)
else:
   print("Fibonacci sequence:-")
   while count < number:
       print(x)
       nth = x + y
       # update values
       x = y
       y = nth
       count += 1
