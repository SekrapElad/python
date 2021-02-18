# Doesn't override an index position, 
# it'll just increment the value which was already at that index.

strings = ['test1', 'test3']
strings.insert(1, 'test2')

print(strings)

# Basically just appends a value at a specific index.