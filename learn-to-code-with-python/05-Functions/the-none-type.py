# "None" is an empty object (like "null" in PHP)
a = None

# Type is "<class 'NoneType'>"
print(type(a))

# Every function will return "None" by default, 
# unless a return value is specified.
def subtract(a, b):
    print(a - b)

result = subtract(5, 3)
# Will print "None"
print(result)