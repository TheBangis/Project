# Exercise Day 3
"""" import math

# exercise number 1 - 3 
age = 25
height = 1.92
c_num = 2j

# exercise number 4
b = int(input("enter base: "))
h = int(input("enter height: "))
area = 0.5 * b * h
print("area: {}".format(int(area)))

# exercise number 5
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is {}'.format(perimeter))

# exercise number 6
length = int(input("Length: "))
width = int(input('width: '))
area = length * width
perimeter = 2 * (length + width)
print("area is: {}, perimeter is: {}".format(area, perimeter))

# exercise number 7
r = int(input('enter radius: '))
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print('area is {}, circumference is {}'.format(area, c))

# exercise number 8

# exercise number 9
import math

x1, y1, x2, y2 = 2, 2, 6, 10
m = (y2 - y1) / (x2-x1)
d = math.sqrt((pow((x2-x1), 2) + pow((y2 - y1), 2)))
print('slope is {}, distance is {}'.format(m, d))

#exercise number 10
#exercise number 11

#exercise number 12

print(len('python') == len('dragon'))

#exercise number 13

print('on' in ('python' and 'dragon'))

#exercise number 14

print('jargon' in 'I hope this course is not full of jargon')

#exercise number 15
print('on' not in ('python' and 'dragon'))

#exercise number 16
print(str(float((len('python')))))

#exercise number 17
num = int(input("enter number: "))
if(num % 2 == 0):
    print('{} is even number'.format(num))
else:
    print('{} is not even number'.format(num))

#exercise number 18
print(7 // 3 == int(2.7))

#exercise number 19
print(type('10') == type(10))

#exercise number 20
print(int(9.8) == 10)

#exercise number 21
hours = int(input("enter hours: "))
rate = int(input('rate per hour: '))
weekly_earning = hours * rate
print('Your weekly earning is {}'.format(weekly_earning))

#exercise number 22
years = int(input('enter number of years you have lived: '))
hours = 24
minutes = 60
second = 60
one_year = 365
second_lived = hours * minutes * second * one_year * years
print('You have lived fo {} seconds'.format(second_lived))"""

#exercise number 23
list = [[1, 1, 1, 1, 1],
        [2, 1, 2, 4, 8],
        [3, 1, 3, 9, 27],
        [4, 1, 4, 16, 64],
        [5, 1, 5, 25, 125]
]

for i in list:
    for row in i:
        print(row, end=' ')
    print()