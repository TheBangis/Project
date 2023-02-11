
# Number 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_and_nagetives_nums = [i for i in range(10) if i <=0]
print(zero_and_nagetives_nums)

# Number 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten = [number for row in list_of_lists for number in row]
flatten1 = [number for row in flatten for number in row]
print(flatten1)

# Number 3 numbers = [(i, i * i) for i in range(11)] # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
numbers_tp = [(i *i   ) for i in range(11)]
print(numbers_tp)