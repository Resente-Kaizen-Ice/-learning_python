def add(num1, num2):
    return int(num1 + num2)


def sub(num1, num2):
    return int(num1 - num2)


def mul(num1, num2):
    return int(num1 * num2)


def div(num1, num2):
    return num1 / num2

while True:
    intro = input("start?(Y/N): ")

    if intro.lower() == "n":
        print("thank you!")
        break
    elif intro.lower() == "y":

        sign = input("what sign: ")

        num1 = int(input("first number: "))
        num2 = int(input("second number: "))

        if sign == "+":
            print(str(add(num1, num2)))
        elif sign == "-":
            print(str(sub(num1, num2)))
        elif sign == "*" or sign == "x":
            print(str(mul(num1, num2)))
        elif sign == "/" or sign == "%":
            print(str(div(num1, num2)))
        continue