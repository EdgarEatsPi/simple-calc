#TODO:
#Add better way to input equations
def guess_root(n, b): #(guess_root)^n ~= b
  for a in range(0,1000):
    if a ** n < b:
      pass
    elif a ** n > b:
      return a-1
  return 1000

def nth_root(n, b, k):
  if k == 1:
    return guess_root(n, b):
  return (1 / n) * ((n - 1) * nth_root(k-1) + b / nth_root(k-1) ^ (n - 1))

def math(operation, number1, number2, i=3):
  if operation == "M":
    return number1 * number2
  elif operation == "D":
    return number1 / number2
  elif operation == "A":
    return number1 + number2
  elif operation == "S":
    return number1 - number2
  elif operation == "NRT": #(number2)th root of number1 i iterations
    return nth_root(number1, number2, i)
  elif operation == "PWR":
    return number1 ** number2
  else:
    raise Exception("Sorry, you enetered an invalid value or operation.")


Number1 = float(input("Enter number 1: "))
operationInput = input("Enter an operation (M - Multiplication, D - Division, A - Add, S - Subtract, NRT - Nth Root, PWR - Power): ")
iterations = int(input("Enter the amount of iterations for nth root if selected. Otherwise, just press enter: "))
if iterations == "":
  iterations == 3
Number2 = float(input("Enter number 2: "))
answer = math(operationInput, Number1, Number2, iterations)
print(answer)

useLastAnswer = input("Do you want to reuse the last input in a new operation? (Y - Yes, N - No): ")

while useLastAnswer == "Y":
    Number1 = answer
    operationInput = input("Enter an operation (M - Multiplication, D - Division, A - Add, S - Subtract): ")
    iterations = int(input("Enter the amount of iterations for nth root if selected. Otherwise, just press enter: "))
    if iterations == "":
        iterations == 3
    Number2 = float(input("Enter number 2: "))
    answer = math(operationInput, Number1, Number2)
    print(answer)
    useLastAnswer = input("Do you want to reuse the last input in a new operation? (Y - Yes, N - No): ")
