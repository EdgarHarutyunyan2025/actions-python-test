"""
Модуль для выполнения базовых математических операций:
сложение, вычитание, умножение и деление.
"""

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
    """
    Функция для деления двух чисел.
    Возвращает результат деления или сообщение об ошибке, если деление на ноль.
    """
    if second_number == 0:
        return "Деление на ноль невозможно"
    return first_number / second_number

# Заданные значения (имена переменных должны быть в верхнем регистре)
NUM1 = 10
NUM2 = 5

# Выполнение операций и вывод результатов
print(f"{NUM1} + {NUM2} = {add(NUM1, NUM2)}")
print(f"{NUM1} - {NUM2} = {subtract(NUM1, NUM2)}")
print(f"{NUM1} * {NUM2} = {multiply(NUM1, NUM2)}")
print(f"{NUM1} / {NUM2} = {divide(NUM1, NUM2)}")



