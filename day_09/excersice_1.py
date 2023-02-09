''' 30 Days of Python, Day 09
Exercise 1: Level 1'''

# Number 1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print('You need {}, more years to learn to drive'.format(18 - age))

# Number 2
my_age = 25
your_age = int(input('enter your age: '))
if your_age > my_age:
    if your_age - my_age == 1:
        result = "You are {} year older than me.".format(your_age - my_age)
    else:
         result = "You are {} years older than me.".format(your_age - my_age)
else:
    result = 'you are not older than me.'
print(result)

# Number 3
a = int(input('enter a: '))
b = int(input('enter b: '))
if a > b:
    print('{} is greater than {}'.format(a,b))
elif a < b:
    print('{} is smaller than {}'.format(a,b))
else:
    print('{} is equal to {}'.format(a,b))

