num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide  =  num1 / num2
if operation == "+" :
   print("The result is ",addition)
if operation == "-" :
   print("The result is ",subtract)
if operation == "*" :
   print("The result is ",multiply)
if operation == "/" and num2 == "0" :
   print("Cannot divide by zero.")
if operation == "/"  :
   print("The result is ",divide)         