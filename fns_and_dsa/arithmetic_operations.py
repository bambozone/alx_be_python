# def greet(name):
# """Prints a greeting message."""
# print(f"Hello, {name}!")
from arithmetic_operations import perform_operation

def main():
   
  def perform_operation(num1, num2, operation):
    if operation == "add":
          return num1 + num2
    if operation == "substract":
           return num1 - num2
    if operation == "multiply":
           return num1 * num2
    if operation == "divide":
           return num1 / num2 
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")







if __name__ == "__main__":
    main()