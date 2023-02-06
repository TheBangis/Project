''' 30 Days of Python, Day 10
Exercise 2: Level 2'''

# Number 1
Sum = 0
for i in range(101):
    Sum = Sum + i
print('The sum of all numbers is ', Sum)


# Number 2
s_even = 0
s_odd = 0
for x in range(101):
    if x % 2 == 0:
        s_even = s_even + x
    else:
        s_odd = s_odd + x
print('The sum of all evens is {}. And the sum of all odds is {}.'.format(s_even, s_odd))

