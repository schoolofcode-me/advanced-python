def divide_secure(number, divisor):
    assert divisor != 0, "Divided a number by zero!"
    return number / divisor

print(divide_secure(10, 0))