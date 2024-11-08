def add(first_number, second_number):
    """
    Функция для сложения двух чисел.
    """
    return first_number + second_number

def subtract(first_number, second_number):
    """
    Функция для вычитания двух чисел.
    """
    return first_number - second_number

def multiply(first_number, second_number):
    """
    Функция для умножения двух чисел.
    """
    return first_number * second_number

def divide(first_number, second_number):
    if second_number == 0:
        return "Деление на ноль невозможно"
    return first_number / second_number

NUM1 = 10
NUM2 = 5

print(f"{NUM1} + {NUM2} = {add(NUM1, NUM2)}")
print(f"{NUM1} - {NUM2} = {subtract(NUM1, NUM2)}")
print(f"{NUM1} * {NUM2} = {multiply(NUM1, NUM2)}")
print(f"{NUM1} / {NUM2} = {divide(NUM1, NUM2)}")



