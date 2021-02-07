# Every numeric value except for 0 returns TRUE 
# in an if statement:

if 1:
    print("1 is a truthy value!")

if 0:
    print("0 is a falsy value, so it won't print!")

if 3:
    print("3 is a truthy value!")

if -3:
    print("-3 is also a truthy value!")


# Every string value except for "" returns TRUE 
# in an if statement:

if "djncd":
    print("Truthy")

if "":
    print("False?")

# Can check this with bool() function.
print(bool(2))
print(bool(0))

var = 3

print()