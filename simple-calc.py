print("Python Calculator\nEnter \"quit\" or \"exit\" to exit the program")

while True:
    equation = input("")
    if (equation == "quit") or (equation == "exit"):
        break
    solution = eval(equation)
    print(solution)

print("Exiting program...")
