def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
n =int(input("enter the number"))
if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", n, "is", recur_factorial(n))
