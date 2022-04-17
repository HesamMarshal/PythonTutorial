##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# Match Case                             #
##########################################

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter the operator: ")


match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "**" | "^":
        print(a**b)
    case _:
        print("Error")
