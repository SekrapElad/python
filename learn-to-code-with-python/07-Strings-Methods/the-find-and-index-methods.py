browser = "Google Chrome"

# If found, it prints the index 
# where the found string starts.
print(browser.find("C"))
print(browser.find("Chrome"))

# If not found, returns -1.
print(browser.find("sldkcns"))

# Can also use offset, 
# returns the index from start of string.
print(browser.find("o", 5))


print(browser.find("o"))