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
