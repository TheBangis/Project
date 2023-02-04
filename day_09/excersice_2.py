
''' 30 Days of Python, Day 09
Exercise 2: Level 2

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
u_input = str(input("enter month: "))
if u_input == 'september' or u_input == 'october' or u_input == 'november':
    print('The season is Autumn.')
elif u_input == 'december' or u_input == 'january' or u_input == 'february':
    print('The season is Winter')
elif u_input == 'march' or u_input == 'april' or u_input == 'may':
     print('The season is Spring')
elif u_input == 'june' or u_input == 'july' or u_input == 'august':
    print('The season is Summer')
else:
    print('Try Again!')


# Number 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('fruit name: '))
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits) '''

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210' }
    }

skill_length = len(person['skills'])
if 'skills' in person:
    if skill_length % 2 == 0:
        mid_1 = person['skills'][skill_length // 2]
        mid_2 = person['skills'][skill_length // 2 - 1]
        result = 'The middle items are {} & {}'.format(mid_1, mid_2)
    else:
         mid_1 = person['skills'][skill_length // 2]
         result = 'The middle item is {} '.format(mid_1)  
print(result)

skill = person['skills']
if 'skills' in person:
    if 'Python' in skill:
        print('Person has Python skill')







