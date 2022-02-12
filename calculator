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

def first_calculation():
  num1 = int(input("What is the first number? "))
  num2 = int(input("What is the second number? "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation symbol. ")
  selected_operation = operations[operation_symbol]
  print(f"{num1} {operation_symbol} {num2} = {selected_operation(num1, num2)}")
  return selected_operation(num1, num2)
  

def additional_calculation():
  previousN = result
  nextN = int(input("What is the second number? "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation symbol. ")
  selected_operation = operations[operation_symbol]
  print(f"{previousN} {operation_symbol} {nextN} = {selected_operation(previousN, nextN)}")
  return selected_operation(previousN, nextN)

continue_calculation = True
first = True
result = 0

while continue_calculation:
  if first == True:
    result = first_calculation()
    first = False
  else:
    result = additional_calculation()
  proceed = input(f"Type 'y' to continue calculating with {result}. Type 'n' to start a new caclulation. ")
  first = False
  if proceed == "n":
    clear()
    first = True
    result = 0
