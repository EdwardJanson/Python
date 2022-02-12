from replit import clear

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide,
  }

def calculator():
  num1 = float(input("What is the first number? "))
  for symbol in operations:
    print(symbol)

  continue_calculation = True

  while continue_calculation:
    operation_symbol = input("Pick an operation symbol. ")
    num2 = float(input("What is the next number? "))
    selected_operation = operations[operation_symbol]
    result = selected_operation(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")
    proceed = input(f"Type 'y' to continue calculating with {result}. Type 'n' to start a new caclulation. ")
    if proceed == "y":
      num1 = result
    else:
      continue_calculation = False
      clear()
      calculator()

calculator()
