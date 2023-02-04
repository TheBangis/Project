''' 30 Days of Python, Day 09
Exercise 3: Level 3'''


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
    else:
        print('Person has no Python skill')

if person['is_marred'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']))
    