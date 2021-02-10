haystack = [3, 4, 6, 7, 8, 9]

def contains(needle, haystack):
    found = False
    for hay in haystack:
        if hay == needle:
            found = True
            break
    return found

print(contains(4, haystack))