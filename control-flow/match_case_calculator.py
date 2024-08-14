num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
#identifying operations
addition = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide  =  num1 / num2
match operation :
      case "+" :
            print("The result is ",addition)
      case "-" :
            print("The result is ",subtract)
      case "/" :
            if num2 == 0 :
               print("Cannot divide by zero ")
            else :
               print("The result is ",divide)

      case "*" :
            print("The result is ",multiply)
      case other :
            print("The result is ",addition)
                      