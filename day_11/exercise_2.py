''' 30  Days od Python - Day 11
Excercise 2: Level 2'''

# Number 1 
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens+=1
        else: 
             odds+=1
    return f" The numbers of evens are {evens}, \n The numbers of odds are {odds}"
print(evens_and_odds(100))

# Number 2
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact
print(factorial(6))

# Number 3
def is_empty(n):
  if len(n) == 0:
    check = 'Empty'
  else:
    check = 'Not empty'
  return check
print(is_empty(()))

# Number 4

