''' 30DaysOfPython
Exercise - Level 1, Day 06: Tuple'''

# Number 01
empty_tuple = ()

# Number 02
sisters = 'hafsa', 'ummulkhairi', 'amina', 'ummi', 'halima', 'rukayyah'
brothers = 'ibrahim', 'hamza', 'abubakar', 'halifa', 'mubarak'
siblings = sisters + brothers
print(siblings)

# Number 03
siblings_count = len(siblings)
print(siblings_count)

# Number 04

list_siblings = list(siblings)
list_siblings.append('sani')
list_siblings.append('jamila')
family_members = tuple(list_siblings)
print(family_members)
