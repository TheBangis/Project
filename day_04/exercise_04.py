# exercise day 04

# number 1
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
space = ' '
sentence = str1 + space + str2 + space + str3 + space + str4
print(sentence)

#number 2
str_1 = 'Coding'
str_2 = 'For'
str_3 = 'All'
statements = str_1 + space + str_2 + space + str_3
print(statements)

# number 3 - 9
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
print(company[0:6])
statement_index = 'Coding Coding For All'
check_index = 'Coding'
print(statement_index.index(check_index)) #or print('Coding' in 'Coding Coding For All')
f_string = 'coding for all'
print(f_string.replace('coding', 'python')) # or print('coding for all'.replace('coding', 'python'))
print('Python for Everyone'.replace('Everyone', 'All'))
print('Coding For All'.split(' '))
tech_firm = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_firm.split(','))

#number 15-17
challenge = 'Coding For All'
print(challenge[0])
print(challenge[-1])
print(challenge[10])

#18-19

print(challenge.index('C'))
print(challenge.index('F'))

print('Coding For All People'.rfind('l'))

s_challenge = 'You cannot end a sentence with because because because is a conjunction'
print(s_challenge.find('because'))
print(s_challenge.rfind('because'))
print(s_challenge[31:54])
print(challenge.startswith('Coding'))
print(challenge.startswith('coding'))

r_char = '   Coding For All      '
print(r_char.strip('   '))

# Number 31
check_1, check_2 = '30DaysOfPython', 'thirty_days_of_python'
print(check_1.isidentifier())
print(check_2.isidentifier())

# Number 32
lists = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
result = '# '.join(lists)
print(result)

# Number 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# Number 34
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# Number 35 
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius 10 is {} meters square.'.format(area))

# Number 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))