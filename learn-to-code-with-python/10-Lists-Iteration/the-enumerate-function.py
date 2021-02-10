list_strings = ['Hello', 'my', 'name', 'is', 'Dale']

for index, string in enumerate(list_strings):
    print(f"{string} is number {index+1} in the list.")

print('\n')

for index, string in enumerate(list_strings, 1):
    print(f"{string} is number {index} in the list.")
