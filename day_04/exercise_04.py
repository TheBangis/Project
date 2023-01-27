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

#number 
challenge = 'Coding For All'
print(challenge[0])
print(challenge[-1])
print(challenge[10])
