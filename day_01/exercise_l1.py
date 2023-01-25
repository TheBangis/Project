#Day_1 30 Days of Python Code
#Exercise : Level 01
import math

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

name = 'Babangida Sani'
f_name = 'Mai Rodi'
country = 'Nigeria'
note = 'I am enjoying 30 days of python'

print('\n')

print(name)
print(f_name)
print(country)
print(note)

print('\n')

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(f_name))
print(type(country))

print('\n')
#Exercise 3, No 2.
#Eculidian Distance between (2, 3) and (10, 8)

x1, x2 = 2, 10
y1, y2 = 3, 8
d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print('Euclidian Distance: {}'.format(d))