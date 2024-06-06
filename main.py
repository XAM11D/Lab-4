def task1(a, b, c):
    return max(a, b, c)


def task2(numbers):
    return sum(numbers)


def task3(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def task4(string):
    return string[::-1]


def task5(n):
    if n == 0:
        return 1
    else:
        return n * task5(n-1)


def task6(number):
    return 25 <= number <= 50


def task7(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


def task8(lst):
    return list(set(lst))


def task9(lst):
    return [num for num in lst if num % 2 == 0]


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


sample_list = (8, 2, 3, 0, 7)
sample_string = "1234abcd"
sample_integer = 3
sample_integer_2 = 512
sample_string_2 = 'The quick Brow Fox'
sample_list_1 = [1, 2, 3, 3, 3, 3, 4, 5]
sample_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(task1(3, 7, 2))       
print(task2(sample_list))   
print(task3(sample_list))   
print(task4(sample_string)) 
print(task5(sample_integer))
print(task6(sample_integer_2))    
print(task7(sample_string_2))     
print(task8(sample_list_1))    
print(task9(sample_list_2))    

n = 7 
print("Maximum number in the last row of Pascal's Triangle with", n, "rows:", task10(n))
