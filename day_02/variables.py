# Day 2: 30 Days of python programming

first_name = 'Babangida'
last_name = 'Sani'
full_name = 'Babangida Sani'
country = 'Nigeria'
city = 'kano'
age = 25
year = 1997
is_married =    False
is_true = 'no'
is_light = 0
is_single, status, phone_no = True, 1, 7039210610

print('Exercises: Level 2', '\n')

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(is_single))
print(type(status))
print(type(phone_no))

print('\n', '# No 2', '\n')

print(len(first_name))
print(len(first_name) == len(last_name))
num_one  = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two

print('\n', 'Area of Circle', '\n')

radius = 30
area_of_circle = 3.143 * pow(radius, 2)
print('Area of Circle: {}'.format(area_of_circle))

print('\n', 'Circumference of a circle', '\n')
circum_of_circle = 2 * 3.143 * radius
print("Circumference of a circle: {}".format(circum_of_circle))

print('\n', 'Area of Circle, Take user input', '\n')

radius = int(input("enter radius: "))
area = 3.143 * pow(radius, 2)
print('Area of Circle: {}'.format(area))

print('\n', 'build-in input', '\n')
first_name = str(input("enter first name: "))
last_name = str(input("enter last name: "))
country= str(input("enter country: "))
age = int(input('enter age: '))
