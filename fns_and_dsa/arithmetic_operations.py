

   
def perform_operation(num1, num2, operation):
    if operation == "add":
       return num1 + num2
    elif operation == "subtract":
       return num1 - num2
    elif operation == "multiply":
       return num1 * num2
    elif  num2 == 0 and operation == "divide"  :
       return "Error: Division by zero is not allowed."
    elif operation == "divide" and num2 != 0 :
       return num1 / num2








    