# Diff between extend and append:
# Append will only append 1 item to a list.
# Extend will append multiple items to a list.

strings = ["Test1", "Test2"]
strings.extend(["Test3", "Test4"])
print(strings)