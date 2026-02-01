import math

def factorial(num):
    if type(num) != int:
        return None;
    if num <0:
        return None;
    if num == 0 or num == 1:
        return 1;
    return num * factorial(num -1)

user_input = input("Enter a number : ")

if user_input.isdigit():
    number = int(user_input)
    print(factorial(number))
else:
    print(factorial(user_input))