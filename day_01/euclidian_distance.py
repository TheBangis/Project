import math
#Exercise 3, No 2.
#Eculidian Distance between (2, 3) and (10, 8)

x1, x2 = 2, 10
y1, y2 = 3, 8
d = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
print('Euclidian Distance: {}'.format(d))