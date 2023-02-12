''' 30 Day days of Python : Day 13
Exercises: Comprehension list'''

# Number 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_and_nagetives_nums = [i for i in numbers if i <=0]
print(zero_and_nagetives_nums)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [number for row in list_of_lists for number in row]
flatten1 = [number for row in flatten for number in row]
print(flatten1)

# Number 3. numbers = [(i, i * i) for i in range(11)] # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
a = [(i**1,i**0,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(a)

# Number 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_list= [[lst[0].upper(), lst[0][:3].upper(), lst[1].upper()] for row in countries for lst in row]
print(flatten_list)

# Number 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict = [{'country':dic[0], 'city':dic[1]} for row in countries for dic in row]
print(dict)

# Number 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_name = [(name[0] + ' ' + name[1]) for row in names for name in row ]
print(full_name)

# Number 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# y = mx+c
#  slope = m 
y = lambda m, x, c:m
print(y(3,6,7))
