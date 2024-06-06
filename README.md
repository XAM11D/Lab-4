# Lab-4
Лабораторна робота 4: Робота з функціями в Python

Мета роботи
Мета цієї лабораторної роботи - вивчення роботи з функціями у Python, які виконують різні типи завдань: обчислення максимального значення, суми та добутку чисел, обробка рядків, рекурсивні функції, перевірка умов, підрахунок кількості великих та малих літер, робота з множинами, відбір парних чисел та робота з трикутником Паскаля. Очікувані результати включають написання та тестування функцій, що виконують ці завдання.

Опис завдання
Завдання 1: Написати функцію, яка повертає максимальне з трьох чисел.
Завдання 2: Написати функцію, яка повертає суму чисел у списку.
Завдання 3: Написати функцію, яка повертає добуток чисел у списку.
Завдання 4: Написати функцію, яка повертає перевернутий рядок.
Завдання 5: Написати рекурсивну функцію, яка обчислює факторіал числа.
Завдання 6: Написати функцію, яка перевіряє, чи знаходиться число в діапазоні від 25 до 50 включно.
Завдання 7: Написати функцію, яка підраховує кількість великих та малих літер у рядку.
Завдання 8: Написати функцію, яка повертає список без дублюючих елементів.
Завдання 9: Написати функцію, яка повертає список парних чисел.
Завдання 10: Написати функцію, яка обчислює максимальне число в останньому ряду трикутника Паскаля з заданою кількістю рядів.

Виконання роботи

Завдання 1:
def task1(a, b, c):
    return max(a, b, c)

# Приклад використання:
print(task1(3, 7, 2))  # Виведе: 7

Завдання 2:
def task2(numbers):
    return sum(numbers)

# Приклад використання:
sample_list = (8, 2, 3, 0, 7)
print(task2(sample_list))  # Виведе: 20

Завдання 3:
def task3(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Приклад використання:
sample_list = (8, 2, 3, 0, 7)
print(task3(sample_list))  # Виведе: 0

Завдання 4:
def task4(string):
    return string[::-1]

# Приклад використання:
sample_string = "1234abcd"
print(task4(sample_string))  # Виведе: "dcba4321"

Завдання 5:
def task5(n):
    if n == 0:
        return 1
    else:
        return n * task5(n-1)

# Приклад використання:
sample_integer = 3
print(task5(sample_integer))  # Виведе: 6

Завдання 6:
def task6(number):
    return 25 <= number <= 50

# Приклад використання:
sample_integer_2 = 512
print(task6(sample_integer_2))  # Виведе: False

Завдання 7:
def task7(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Приклад використання:
sample_string_2 = 'The quick Brow Fox'
print(task7(sample_string_2))  # Виведе: (3, 12)

Завдання 8:
def task8(lst):
    return list(set(lst))

# Приклад використання:
sample_list_1 = [1, 2, 3, 3, 3, 3, 4, 5]
print(task8(sample_list_1))  # Виведе: [1, 2, 3, 4, 5]

Завдання 9:
def task9(lst):
    return [num for num in lst if num % 2 == 0]

# Приклад використання:
sample_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(task9(sample_list_2))  # Виведе: [2, 4, 6, 8]

Завдання 10:
def task10(n):
    def generate_pascals_triangle(num_rows):
        triangle = [[1]]
        for _ in range(1, num_rows):
            prev_row = triangle[-1]
            next_row = [1]  
            for j in range(1, len(prev_row)):
                next_row.append(prev_row[j - 1] + prev_row[j])  
            next_row.append(1)  
            triangle.append(next_row)
        return triangle

    triangle = generate_pascals_triangle(n)
    last_row = triangle[-1]
    return max(last_row)

# Приклад використання:
n = 7
print("Maximum number in the last row of Pascal's Triangle with", n, "rows:", task10(n))  # Виведе: 21


Приклади виводу програми:
Завдання 1: 7
Завдання 2: 20
Завдання 3: 0
Завдання 4: "dcba4321"
Завдання 5: 6
Завдання 6: False
Завдання 7: (3, 12)
Завдання 8: [1, 2, 3, 4, 5]
Завдання 9: [2, 4, 6, 8]
Завдання 10: 21

Вимоги до середовища:Python 3.x
