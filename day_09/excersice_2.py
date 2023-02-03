
''' 30 Days of Python, Day 09
Exercise 2: Level 2'''

# Number 1
marks = int(input('enter marks: '))
if marks <= 49:
    grade = 'F'
elif marks <= 59:
    grade = 'D'
elif marks <= 69:
    grade = 'C'
elif marks <= 79:
    grade = 'B'
elif marks <= 100:
    grade = 'A'
else:
    grade = 'Out of range'
print(grade)


# Number 2
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('fruit name: '))
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
