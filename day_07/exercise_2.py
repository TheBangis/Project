''' 30 Days Of Python: Day 7 - Sets
Exercise: Level 2
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Number 1
print(A.union(B))

# Number 2
print(A.intersection(B))

# Number 3
print(A.issubset(B))

# Number 4
print(A.isdisjoint(B))

# Number 5
A_B = A.union(B)
B_A = B.union(A)
print('A join with B is ', A_B, 'and B join with A is ', B_A)

# Number 6
print(A.symmetric_difference(B))

# Number 7
del A
del B
