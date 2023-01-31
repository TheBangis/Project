# 30 Days Of Python: Day 7 - Sets

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Number 01
companies_len = len(it_companies)

# Number 02
it_companies.add('Twitter')

# Number 03
it_companies.update(['Slack', 'Telegram', 'ChatGTP'])

# Number 04
it_companies.pop()

# Number 05
# Ans: Remove raise an error if the item doesn't exist in the set while discard do not arise error.
print(companies_len)
print(it_companies)