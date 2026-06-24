def add(n1, n2) :
    return n1 + n2


def sub(n1, n2) :
    return n1 - n2


def mult(n1, n2) :
    return n1 * n2


def div(n1, n2) :
    return n1/n2


num1 = int(input("Enter number: "))
num2 = int(input("Enter number: "))


print("Sum: ", add(num1, num2))
print("Difference: ", sub(num1, num2))
print("Multiplication: ", mult(num1, num2))
print("Division: ", div(num1, num2))

