''' 30DaysOfPython
Exercise - Level 2, Day 06: Tuple'''

# Number 01
fruits = ('mango', 'banana', 'apple')
vegetables = ('salat', 'carrot')
animal_products = ('dog', 'cat', 'goat')

# Number 02
food_stuff_tp = fruits + vegetables + animal_products

# Number 03
food_stuff_lt = list(food_stuff_tp)

# Number 04
food_length = len(food_stuff_lt)
if food_length % 2 == 0:
    middle_x = food_stuff_lt[food_length // 2]
    middle_y = food_stuff_lt[food_length // 2 - 1]
    print('middle items are {} & {}'.format(middle_x, middle_y))
else:
    middle_item = food_stuff_lt[food_length // 2]
    print('middle item is {}'.format(middle_item))

# Number 05
print('first 3 are ', food_stuff_lt[0:3], 'last 3 are ', food_stuff_lt[-3::])

# Number 06
del food_stuff_tp

''' Number 07
chk_itm = 'banana' in food_stuff_tp
print(chk_itm)'''


'''
- Check if 'Estonia' is a nordic country
- Check if 'Iceland' is a nordic country'''

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

chk_ctry1 = 'Estonia' in nordic_countries
chk_ctry2 = 'Iceland' in nordic_countries
print(chk_ctry1)
print(chk_ctry2)