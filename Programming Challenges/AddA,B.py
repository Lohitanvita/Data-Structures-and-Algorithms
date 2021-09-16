# python3
#sum_of_two_digits

def add_two_numbers(number1, number2):
    return number1 + number2

a, b = map(int, input().split())
print("sum:",add_two_numbers(a, b))
