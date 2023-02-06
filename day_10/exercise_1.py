''' 30 Days of Python, Day 10
Exercise 1: Level 1'''

# Number 1
for i in range(11):
    print(i)

count = 0
while count < 11:
    print(count)
    count+=1
else:
    print("The iteration stop at", count)

# Number 2
for i in range(10, -1, -1):
    print(i)

x = 10
while x >= 0:
    print(x)
    x-=1

# Number 3

# Number 4
for i in range(8):
    for x in range(7):
        print('#', end='')
    print("#")

# Number 5
mul = 0
while mul < 11:
    print('{} * {} = {}'.format(mul, mul, mul*mul))
    mul+=1

# Number 6
lst =  ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for i in lst:
    print(i)
    

# Number 7
for even in range(0, 101, 2):
    print(even)

# Number 8
for odd in range(0, 100, 1):
    if odd % 2 == 0:
        continue
    print(odd)


