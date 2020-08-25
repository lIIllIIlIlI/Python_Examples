# 1. List comprehension instead of for/if loop combination
# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]
print(result)
# [0, 4, 16, 36, 64]

# 2. enumerate to prevent nested for loop
for index, variable in enumerate(result):
    print("Variable {} with index {}".format(index, variable))
