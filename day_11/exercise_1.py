''' 30  Days od Python - Day 11
Excercise 1: Level 2'''

# Number 1
def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(4,6))

# Number 2
def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area
print(area_of_circle(30))

# Number 3  

def add_all_nums(*nums):
    total = 0
    for i in nums:
        total+=i
    return total
print(add_all_nums(1,5,3,1))

# Number 4

def convert_celsius_to_fahrenheit(C = 23):
    F = (C * 9/5) + 32
    return F
print(convert_celsius_to_fahrenheit())

# Number 5
def check_season(month):
    if month in ['june', 'august', 'october']:
        season = "Autumn"
    elif month == 'july':
        season = 'Winter'
    elif month == 'september':
        season = 'Spring'
    elif month == 'january':
        season = "Summer"
    else:
        season = 'try again'
    return season
print(check_season('august'))

# Number 6
def calculate_slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print(calculate_slope(2,3,4,5))

# Number 7
import math
def solve_quadratic_eqn(a, b, c):
    x1 = ((-b) + math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    x2 = ((-b) - math.sqrt(pow(b,2) - 4 * a * c)) / (2 * a)
    result = 'x1 = {} and x2 = {}'.format(x1, x2)
    return result
print(solve_quadratic_eqn(1, -5, 6))

# Number 8
def print_list(lst):
    for i in lst:
        print(i) 
print_list(['banana', 'mango', 'apple'])

# Number 9
def reverse_list(lst):
    rev_lists = []
    for i in range(len(lst)-1, -1, -1):
        rev_lists.append(lst[i])
    return rev_lists
print(reverse_list(['python', 'is', 'fun']))

# Number 10
def capitalize_list_items(lst):
    cap_lists = []
    for i in range(len(lst)):
        cap_lists.append(lst[i].capitalize())
    return cap_lists
print(capitalize_list_items(['boy', 'girl', 'man', 'woman']))


# Number 11
def add_item(lst, item):
    lst.append(item)
    return lst
print(add_item([2,3,4,5], 6))

# Number 12
def remove_item(lst, item):
    lst.remove(item)
    return lst
print(remove_item([3,4,6,7], 4))

# Number 13
def sum_of_numbers(n):
    sum_n = 0
    for i in range(n + 1):
        sum_n+=i
    return sum_n
print(sum_of_numbers(10))

# Number 14
def sum_of_odds(odd):
    sum_of_odd = 0
    for i in range(odd + 1):
        if i % 2 != 0:
            sum_of_odd+=i
    return sum_of_odd
print(sum_of_odds(5)) 

# Number 15
def sum_of_evens(even):
    even_s = 0
    for i in range(0, even + 1, 2):
        even_s+=i
    return even_s
print(sum_of_evens(10))

