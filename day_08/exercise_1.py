''' 30 Days Of Python: Day 8 - Sets
Exercise: Level 2
'''
# Number 1
dog = {}

# Number 2
dog['name'] = 'jupyter'
dog['color'] = 'black'
dog['breed'] = 'mammial'
dog['legs'] = 2
dog['age'] = 6

# Number 3

student = {'first_name': 'babangida', 'last_name': 'sani', 'gender':'male', 'age':25,
 'marital status':'married', 'skill': ['htmt', 'css', 'python'], 'country': 'nigeria', 
 'city':'kano', 'address':{'no': 1212, 'street': 'dan rimi'}}

# Number 4
student_len = len(student)
print(student_len)

# Number 5
get_skill = student['skill']
print(type(get_skill))

# Number 6
student['skill'].append('java')
student['skill'].append('maths')
print(student['skill'])

# Number 7
keys = student.keys()
print(keys)

# Number 8
values = student.values()
print(values)

# Number 9
list_tp = student.items()
print(list_tp)

# Number 10
del student['age'] # or student.pop('skill')
print(student)

# Number 11
del student