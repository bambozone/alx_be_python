

   
def perform_operation(num1, num2, operation):
    if operation == "add":
       return num1 + num2
    elif operation == "subtract":
       return num1 - num2
    elif operation == "multiply":
       return num1 * num2
    elif operation == "divide" and num2 == 0 :
       return "Error: Division by zero is not allowed."
    elif operation == "divide" and num2 != 0 :
       return num1 / num2


print("Arithmetic Operations")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

result = perform_operation(num1, num2, operation)
print(f"Result: {result}")







    