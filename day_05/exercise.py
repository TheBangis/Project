# Exercise Day 05
""""
# Number 01
lst = []

# Number 02
phones = ['infinix', 'Techno', 'Ridimi', 'iphone', 'nokia', 'google pixel']

# Number 03
length = len(phones)
print(length)

# Number 04
first_item = phones[0]
print(first_item)
middle_item = phones[3]
print(middle_item)
last_item = phones[-1]
print(last_item)

# Number 05
mixed_data_types = ['babangida', '25', '1.91', 'single', 'dan rimi']

# Number 06
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Number 07
print(it_companies)

# Number 08
print(len(it_companies))

# Number 09
first_company = it_companies[0]
print(first_company)
second_company = it_companies[3]
print(second_company)
last_company = it_companies[-1]
print(last_company)

# Number 10
it_companies[1] = 'ChatGPT'
print(it_companies)

# Number 11
it_companies.append('Ubuntu')
print(it_companies)

# Number 12
it_companies.insert(4, 'Shamrock')
print(it_companies)

# Number 13
it_companies[0] = 'FACEBOOK'
print(it_companies)

# Number 14

# Number 15
does_exist = 'Facebook' in it_companies
print(does_exist)

# Number 16
it_companies.sort()
print(it_companies)

# Number 17
it_companies.reverse()
print(it_companies)

# Number 18
print(it_companies[0:3])

# Number 19
print(it_companies[-3::])

# Number 20
print(it_companies[4:9:5])

# Number 21
it_companies.pop(0)
print(it_companies)

# Number 22
del it_companies[3]
print(it_companies)

# Number 23
it_companies.pop()
print(it_companies)

# Number 24
it_companies.clear()
print(it_companies)

# Number 25
del it_companies

# Number 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# Number 27
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)"""

""" Challenge: 
Exercise (2) Day 05"""

# Number 01

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)