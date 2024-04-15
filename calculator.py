#!/usr/bin/env python3


def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Can't divide by zero!"
    return a / b

def power_of(a, b):
    return a ** b

def modulos(a, b):
    return a % b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_odd_even(num):
    return "Odd" if num % 2 != 0 else "Even"

def is_div_by_five(num):
    return num % 5 == 0

def validate_num(str_input):
    str_input = str_input.replace('+', '')
    str_input = str_input.strip()
    return str_input.replace('-', '', 1).isdigit()

def get_num_input(prmpt):
    while True:
        user_input = input(prmpt)
        if validate_num(user_input):
            return int(user_input)
        else:
            print("Invalid input! Please use valid integers, positive and negative.")

def op_menu():
    menu = """
    Welcome to Calculator! :)
    a. Add
    b. Substract
    c. Multiply
    d. Divide
    e. Power of
    f. Modulos
    g. Exit
    Please choose and operation:
    """
    while True:
        op = input(menu).lower()
        if op in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            return op
        else:
            print("Invalid choice! Please choose an operation from thr menu.")

def main():
    while True:
        op = op_menu()

        if op == 'g':
            print("Exiting the Calculator... Goodbye! :)")
            break
        
        num1 = get_num_input("Enter the first number: ")
        num2 = get_num_input("Enter the second number: ")

        if op == 'a':
            result = add(num1, num2)
        elif op == 'b':
            result = substract(num1, num2)
        elif op == 'c':
            result = multiply(num1, num2)
        elif op == 'd':
            if num2 == 0:
                print("Can't divide by zero!")
                continue
            result = divide(num1, num2)
        elif op == 'e':
            result = power_of(num1, num2)
        elif op == 'f':
            result = modulos(num1, num2)
        
        print(f"Result: {result}")
        print("Prime Number:" , "Yes" if is_prime(result) else "No")
        print(f"Even/Odd: {is_odd_even(result)}")
        print(f"Divisible by 5:" , "Yes" if is_div_by_five(result) else "No")


if __name__ == "__main__":
    main()
